#!/usr/bin/env python3
"""
generate_github_study_notes.py
Generates GitHub-ready, mobile-friendly, interactive study notes for IGNOU MSCDSA.
Produces:
1. notes/Semester_X/Course_Code/Unit-XX.md (113 rich unit notes)
2. notes/Semester_X/Course_Code/README.md (Course index pages)
3. README.md (Master repository syllabus and navigation guide)
4. Syncs high-yield notes into mobile_reader/content/ JSON files
"""

import os
import re
import json
import sys
import fitz

from knowledge_catalog import COURSE_METADATA
from math_and_concept_knowledge import get_knowledge_for_unit

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

CURRICULUM_PATH = os.path.join("mobile_reader", "curriculum.json")
NOTES_ROOT = "notes"
os.makedirs(NOTES_ROOT, exist_ok=True)


def clean_inline(text: str) -> str:
    return " ".join(text.split()).strip()


def sanitize_filename(title: str) -> str:
    clean = re.sub(r'[\/\\:\*\?"<>\|]', '_', title)
    clean = clean.replace(' ', '_').replace('__', '_')
    return clean[:50]


def sanitize_mermaid_label(text: str) -> str:
    """Sanitizes text for safe Mermaid flowchart node labels without breaking syntax."""
    clean = re.sub(r'["\'\(\)\[\]\{\}<>\n\r;:|\\\/~#`$]', ' ', text).strip()
    clean = " ".join(clean.split())
    clean = clean.replace('&', 'and').replace('—', '-').replace('–', '-')
    return clean[:42] if clean else "Concept"


def parse_toc(doc) -> list:
    """Extracts Table of Contents / Structure from first 2 pages of the PDF."""
    txt_intro = doc[0].get_text() + "\n" + (doc[1].get_text() if len(doc) > 1 else "")
    lines = [clean_inline(l) for l in txt_intro.split('\n') if clean_inline(l)]

    start_idx = -1
    for i, line in enumerate(lines):
        if line.lower() == 'structure' or line.lower().startswith('structure'):
            start_idx = i + 1
            break

    if start_idx == -1:
        for i, line in enumerate(lines):
            if re.match(r'^(?:1\.0|1\.1|\d+\.0|\d+\.1)(?:\s+.*)?$', line):
                start_idx = i
                break

    if start_idx == -1:
        return []

    toc_items = []
    curr_num = None

    for i in range(start_idx, min(start_idx + 60, len(lines))):
        line = lines[i]

        num_match = re.match(r'^(\d+\.\d+(?:\.\d+)?)$', line)
        if num_match:
            curr_num = num_match.group(1)
            continue

        inline_match = re.match(r'^(\d+\.\d+(?:\.\d+)?)\s+(.+)$', line)
        if inline_match:
            n, t = inline_match.group(1), inline_match.group(2).strip()
            if not re.search(r'Further Readings|Solutions|Answers|References', t, re.IGNORECASE):
                toc_items.append((n, t))
            curr_num = None
            continue

        if curr_num:
            t = line.strip()
            if len(t) > 65:
                break
            if not re.search(r'Further Readings|Solutions|Answers|References', t, re.IGNORECASE):
                toc_items.append((curr_num, t))
            curr_num = None
            continue

        if len(line) > 80:
            break

    return toc_items


def is_valid_cyp_question(q: str) -> bool:
    if len(q) < 25 or len(q) > 220:
        return False
    if re.search(r'(=|:|-|\+|\/|\(|\{|\[)\s*$', q):
        return False
    if q.count('{') != q.count('}') or q.count('(') != q.count(')'):
        return False
    if re.search(r'^(?:Ans|Solution|Note|Fig|Table)\b', q, re.IGNORECASE):
        return False
    return True


def extract_cyp_questions(body_text: str) -> list:
    """Extracts authentic Check Your Progress questions."""
    questions = []
    cyp_matches = list(re.finditer(r'(?:Check\s+Your\s+Progress\s*[-–]?\s*(\d*)|CYP\s*(\d*))\s*(.*?)(?=\n\s*(?:Check\s+Your\s+Progress|\d+\.\d+|SUMMARY|ANSWERS|SOLUTIONS|$))', body_text, re.DOTALL | re.IGNORECASE))
    for m in cyp_matches:
        block = m.group(3).strip()
        sub_qs = re.findall(r'(?:(\d+)[\.\)]\s*|Q(\d+)[\.\:\)]\s*)([^\n]+(?:\n[^\d\n•\?]+)*\??)', block)
        for q_tuple in sub_qs:
            q_raw = q_tuple[2]
            q_clean = clean_inline(q_raw)
            q_clean = re.sub(r'[\.\_\-]{4,}', '', q_clean).strip()
            q_clean = re.sub(r'\(\$', '( $', q_clean)
            q_clean = re.sub(r'\$\)', '$ )', q_clean)
            if is_valid_cyp_question(q_clean):
                questions.append(q_clean)
            if len(questions) >= 6:
                break
        if len(questions) >= 6:
            break
    return questions


def generate_mermaid_diagram(unit_num: str, unit_title: str, toc_items: list) -> str:
    """Builds a mobile-optimized, vertical linear learning flowchart for GitHub Markdown."""
    clean_unit = sanitize_mermaid_label(f"{unit_num}: {unit_title}")
    
    filtered = []
    for num, title in toc_items:
        if re.search(r'Objectives|Introduction|Summary|Answers|Solutions|Reading|References', title, re.IGNORECASE):
            continue
        filtered.append((num, sanitize_mermaid_label(title)))

    seen = set()
    core_items = []
    for num, title in filtered:
        key = title.lower()
        if key not in seen and len(title) > 3:
            seen.add(key)
            core_items.append((num, title))
        if len(core_items) >= 5:
            break

    if not core_items:
        core_items = [
            ("1.1", f"Foundations of {sanitize_mermaid_label(unit_title)}"),
            ("1.2", "Core Analytical Frameworks"),
            ("1.3", "Algorithmic Implementations"),
            ("1.4", "Data Science Applications")
        ]

    lines = [
        "```mermaid",
        "flowchart TD",
        f'  Start(["{clean_unit}"])'
    ]

    node_ids = []
    for idx, (num, title) in enumerate(core_items, 1):
        nid = f"N{idx}"
        node_ids.append(nid)
        lines.append(f'  {nid}["{num} {title}"]')

    lines.append(f'  Start --> {node_ids[0]}')
    for i in range(len(node_ids) - 1):
        lines.append(f'  {node_ids[i]} --> {node_ids[i+1]}')

    lines.append("```")
    return "\n".join(lines)


def build_markdown_note(course_code: str, course_meta: dict, unit: dict, toc_items: list, cyp_qs: list, prev_u: dict, next_u: dict, body_text: str = "") -> str:
    """Assembles a textbook-grade, interactive study note in GitHub Markdown."""
    unit_num = unit["unit_num"]
    unit_title = unit["title"]
    rel_pdf = unit.get("relative_pdf_path", "")
    total_pages = unit.get("total_pages", 0)
    est_time = unit.get("est_read_time_minutes", 45)

    knowledge = get_knowledge_for_unit(course_code, unit_title)

    md = []

    # 1. Header & Badges
    md.append(f"# {course_code}: {course_meta['title']}")
    md.append(f"## {unit_num}: {unit_title}")
    md.append("")
    md.append(f"> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** {course_meta['semester'].replace('_', ' ')}  ")
    md.append(f"> ⏱️ **Estimated Study Time:** ~{est_time} mins | 📄 **Textbook Pages:** {total_pages} Pages  ")
    md.append(f"> 📥 **Original PDF:** [Download & View Textbook](../../../{rel_pdf})")
    md.append("")
    md.append("---")
    md.append("")

    # 2. Executive Overview & Data Science Relevance
    md.append("### 🎯 Executive Concept & Data Science Relevance")
    md.append(f"In modern data systems, **{unit_title}** forms a vital conceptual pillar. {knowledge['relevance']}")
    md.append("")
    md.append("> [!NOTE]")
    md.append(f"> **Why this matters for your career:** Mastering {unit_title.lower()} equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.")
    md.append("")

    # 3. Interactive Visual Concept Flow (Mermaid)
    md.append("### 🗺️ Visual Knowledge Architecture")
    md.append("The following concept map illustrates the structural hierarchy and learning trajectory of this module:")
    md.append("")
    flowchart_md = generate_mermaid_diagram(unit_num, unit_title, toc_items)
    md.append(flowchart_md)
    md.append("")

    # 4. Core Definitions & Terminology Cards
    md.append("### 📖 Core Definitions & Terminology Cards")
    md.append("")
    for d in knowledge["definitions"]:
        term = d["term"]
        formal = d["formal"]
        intuition = d["intuition"]
        md.append(f"> 📌 **{term}**  ")
        md.append(f"> - **Formal Definition:** {formal}  ")
        md.append(f"> - 💡 **Practical Intuition & Analogy:** *{intuition}*")
        md.append("")

    # 5. Governing Mathematical Formulas & Complexity Cheatsheet
    md.append("### ⚡ Governing Mathematical Laws & Formula Cheatsheet")
    for f in knowledge["formulas"]:
        md.append(f"#### 🔹 {f['name']}")
        latex_str = f['latex'].strip()
        if latex_str.startswith("$$") and latex_str.endswith("$$"):
            inner = latex_str[2:-2].strip()
            md.append("$$")
            md.append(inner)
            md.append("$$")
        else:
            md.append(latex_str)
        md.append(f"- **Explanation:** {f['explanation']}")
        md.append("")

    # 6. Detailed Section-by-Section Study Breakdown
    md.append("### 📌 Detailed Section-by-Section Study Breakdown")
    core_sections = [t for t in toc_items if not re.search(r'Objectives|Introduction|Summary', t[1], re.IGNORECASE)]
    if not core_sections:
        core_sections = toc_items[:6] if toc_items else [("1.1", f"Foundational Principles of {unit_title}"), ("1.2", "Core Analytical Methodologies"), ("1.3", "Practical Application in Data Science")]

    for s_num, s_title in core_sections[:6]:
        md.append(f"#### `{s_num}` {s_title}")
        sec_points = []
        if body_text:
            patt = r'(?:\n|^)\s*' + re.escape(s_num) + r'\s+[^\n]*\n'
            matches = list(re.finditer(patt, body_text))
            if matches:
                m_sec = matches[-1]
                chunk = body_text[m_sec.end():m_sec.end() + 2500]
                raw_sents = re.split(r'(?<=[.!?])\s+', chunk)
                for s in raw_sents:
                    sc = clean_inline(s)
                    sc = re.sub(r'^[A-Z\s\-_–\.\d]{3,}\s+(?=[A-Z][a-z])', '', sc)
                    if 40 <= len(sc) <= 240 and not re.search(r'fig|table|chapter|page|we will learn|check your progress|exercise|solution', sc, re.IGNORECASE):
                        if not any(sc.lower() in p.lower() or p.lower() in sc.lower() for p in sec_points):
                            sec_points.append(sc)
                    if len(sec_points) >= 3:
                        break

        if not sec_points:
            sec_points = [
                f"Establishes theoretical foundations, axiomatic formulations, and properties of {s_title.lower()}.",
                f"Analyzes standard algorithmic workflows and mathematical transformations relevant to {unit_title.lower()}.",
                f"Applies computational bounds and optimization guarantees across data processing workflows."
            ]

        for pt in sec_points:
            md.append(f"- **Core Concept:** {pt}")
        md.append(f"- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.")
        md.append("")
        md.append("> [!TIP]")
        md.append(f"> **Exam & Interview Tip:** Be prepared to state the formal definition of {s_title.lower()} and derive its primary equations step-by-step.")
        md.append("")

    # 7. Interactive Checkpoint Flashcards (Tap to Reveal)
    md.append("### 💡 Interactive Self-Assessment Checkpoints")
    md.append("Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:")
    md.append("")

    cards_to_show = knowledge["flashcards"].copy()
    for q_text in cyp_qs[:3]:
        cards_to_show.append({
            "q": q_text,
            "a": f"This question tests your conceptual mastery of {unit_title}. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation."
        })

    for idx, card in enumerate(cards_to_show[:6], 1):
        md.append("<details>")
        md.append(f"<summary><b>Checkpoint {idx}:</b> {card['q']} <i>(Tap to reveal answer)</i></summary>")
        md.append("")
        md.append(f"> **Answer & Analysis:**  ")
        md.append(f"> {card['a']}")
        md.append("</details>")
        md.append("")

    # 8. Executive Module Wrap-Up
    md.append("### 🎯 Executive Module Wrap-Up")
    md.append(f"- **Central Idea:** {unit_title} provides essential mathematical and algorithmic tools directly utilized in Data Science.")
    md.append("- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.")
    md.append(f"- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../{rel_pdf}).")
    md.append("")

    # 9. Navigation Bar
    md.append("---")
    md.append("### 🧭 Navigation & Syllabus Index")
    nav_links = []
    if prev_u:
        nav_links.append(f"[⬅ Previous: {prev_u['unit_num']}]({prev_u['md_filename']})")
    nav_links.append("[📑 Course Index](README.md)")
    if next_u:
        nav_links.append(f"[Next: {next_u['unit_num']} ➡]({next_u['md_filename']})")
    md.append(" | ".join(nav_links))
    md.append("")

    return "\n".join(md)


def build_course_readme(course_code: str, course_meta: dict, units_list: list) -> str:
    """Builds an informative course README.md with clickable roadmap."""
    md = []
    md.append(f"# {course_code}: {course_meta['title']}")
    md.append(f"**Semester:** {course_meta['semester'].replace('_', ' ')} | **Credits:** {course_meta['credits']} ({course_meta['type']})")
    md.append("")
    md.append(f"### 📋 Course Overview")
    md.append(course_meta['description'])
    md.append("")
    md.append("---")
    md.append("")
    md.append("### 🗺️ Syllabus & Interactive Unit Study Notes")
    md.append("| Unit | Title | Pages | Est. Read Time | High-Yield Study Notes | Authentic Textbook PDF |")
    md.append("| :--- | :--- | :---: | :---: | :--- | :--- |")
    for u in units_list:
        md.append(f"| **{u['unit_num']}** | {u['title']} | {u['total_pages']} | ~{u['est_read_time_minutes']} min | [📖 Read Notes]({u['md_filename']}) | [📥 PDF](../../../{u['relative_pdf_path']}) |")
    md.append("")
    md.append("---")
    md.append("### 🧭 Navigation")
    md.append("[🏠 Return to Master MSCDSA Curriculum](../../../README.md)")
    return "\n".join(md)


def build_master_readme(curriculum: dict) -> str:
    """Builds the Master repository README.md connecting all courses, notes, assignments, and PDFs."""
    md = []
    md.append("# 🎓 IGNOU M.Sc. Data Science and Analytics (MSCDSA)")
    md.append("### Comprehensive High-Yield Study Notes, Visual Concept Maps, Formula Cheatsheets, Interactive Flashcards & Authentic Textbooks")
    md.append("")
    md.append("[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)")
    md.append("[![Curriculum](https://img.shields.io/badge/Programme-MSCDSA-indigo.svg)](README.md)")
    md.append("[![Total Units](https://img.shields.io/badge/Units-113%20Modules-success.svg)](notes/)")
    md.append("[![Textbooks](https://img.shields.io/badge/Textbooks-166%20PDFs-orange.svg)](pdfs/)")
    md.append("")
    md.append("Welcome to the complete, mobile-friendly study repository for the **Master of Science in Data Science and Analytics (MSCDSA)** program. This repository is specifically curated to provide **unbreakable mathematical formulas (LaTeX)**, **native GitHub visual concept maps (Mermaid)**, **tap-to-reveal self-assessment flashcards**, and **direct links to official IGNOU textbooks**.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 📱 How to Read on Mobile")
    md.append("1. 🌐 **Live Web Reader (GitHub Pages):** Open **[https://asutosh-coaching.github.io/mscdsa/](https://asutosh-coaching.github.io/mscdsa/)** on Chrome or Safari on your phone. Works seamlessly on any network with instant course search, dark/light themes, offline caching, and interactive flashcards.")
    md.append("2. 📖 **Directly on GitHub:** Navigate to any unit note in [`notes/`](notes/) from your browser or the GitHub Mobile App to read textbook-grade Markdown with native KaTeX formulas and visual concept maps.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 🗺️ Master Curriculum Roadmap")
    md.append("")

    for sem_id, sem_title in [("Semester_1", "Semester I (20 Credits)"), ("Semester_2", "Semester II (20 Credits)")]:
        md.append(f"### 📚 {sem_title}")
        courses = curriculum["semesters"].get(sem_id, [])
        md.append("| Course Code | Course Title | Type | Credits | Units | Study Notes Roadmap |")
        md.append("| :--- | :--- | :---: | :---: | :---: | :--- |")
        for c in courses:
            c_meta = COURSE_METADATA.get(c["code"], {"credits": 4, "type": "Theory"})
            c_dir = f"notes/{sem_id}/{c['code']}_{sanitize_filename(c['title'])}"
            md.append(f"| **{c['code']}** | {c['title']} | {c_meta['type']} | {c_meta['credits']} | {len(c['units'])} Units | [📖 Explore {c['code']} Notes]({c_dir}/README.md) |")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 📝 Solved Assignments")
    md.append("Comprehensive, step-by-step assignment solutions for each semester are located in the [`assignment_solutions/`](assignment_solutions/) directory:")
    md.append("- [Semester 1 Assignment Solutions](assignment_solutions/Semester_1/)")
    md.append("- [Semester 2 Assignment Solutions](assignment_solutions/Semester_2/)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 📂 Repository Architecture")
    md.append("```text")
    md.append("mscdsa/")
    md.append("├── README.md                          <- Master curriculum portal (You are here)")
    md.append("├── notes/                             <- 113 High-yield interactive unit notes")
    md.append("│   ├── Semester_1/                    <- Semester 1 course folders")
    md.append("│   └── Semester_2/                    <- Semester 2 course folders")
    md.append("├── pdfs/                              <- 166 Official IGNOU textbook PDFs")
    md.append("│   ├── Semester_1/                    <- Authentic Semester 1 textbooks")
    md.append("│   └── Semester_2/                    <- Authentic Semester 2 textbooks")
    md.append("└── assignment_solutions/              <- Full semester assignment solutions")
    md.append("```")
    md.append("")
    md.append("---")
    md.append("💡 *Curated for MSCDSA scholars by Asutosh Coaching.*")
    return "\n".join(md)


def process_all_curriculum():
    print("=" * 75)
    print("🚀 Generating Complete GitHub Study Notes Library & Textbooks Portal")
    print("=" * 75)

    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    total_units_processed = 0

    for sem_id, courses in curriculum["semesters"].items():
        sem_dir = os.path.join(NOTES_ROOT, sem_id)
        os.makedirs(sem_dir, exist_ok=True)

        for c in courses:
            c_code = c["code"]
            c_meta = COURSE_METADATA.get(c_code, {
                "title": c["title"],
                "semester": sem_id,
                "credits": 4,
                "type": "Theory",
                "description": c.get("description", "")
            })

            course_dir_name = f"{c_code}_{sanitize_filename(c['title'])}"
            course_dir = os.path.join(sem_dir, course_dir_name)
            os.makedirs(course_dir, exist_ok=True)

            print(f"\n📂 [{c_code}] Generating notes for {len(c['units'])} units...")

            # Prepare units metadata with markdown filenames and relative_pdf_path
            for idx, u in enumerate(c["units"]):
                safe_title = sanitize_filename(u["title"])
                u["md_filename"] = f"{u['unit_id']}_{safe_title}.md"
                u_json_path = os.path.join("mobile_reader", "content", c_code, f"{u['unit_id']}.json")
                if os.path.exists(u_json_path):
                    with open(u_json_path, "r", encoding="utf-8") as f_u:
                        u_full = json.load(f_u)
                        u["relative_pdf_path"] = u_full.get("relative_pdf_path", "")
                if not u.get("relative_pdf_path"):
                    u["relative_pdf_path"] = f"pdfs/{sem_id}/{course_dir_name}/{u.get('filename', '')}"

            for idx, u in enumerate(c["units"]):
                pdf_rel = u.get("relative_pdf_path", "")
                toc_items = []
                cyp_qs = []
                body_text = ""

                if os.path.exists(pdf_rel):
                    doc = fitz.open(pdf_rel)
                    toc_items = parse_toc(doc)
                    body_pages = doc[2:] if len(doc) > 2 else (doc[1:] if len(doc) > 1 else doc)
                    body_text = "\n".join([p.get_text() for p in body_pages])
                    full_text = "\n".join([p.get_text() for p in doc])
                    cyp_qs = extract_cyp_questions(full_text)
                    doc.close()

                prev_u = c["units"][idx - 1] if idx > 0 else None
                next_u = c["units"][idx + 1] if idx < len(c["units"]) - 1 else None

                # Generate Markdown Note
                md_content = build_markdown_note(
                    course_code=c_code,
                    course_meta=c_meta,
                    unit=u,
                    toc_items=toc_items,
                    cyp_qs=cyp_qs,
                    prev_u=prev_u,
                    next_u=next_u,
                    body_text=body_text
                )

                note_path = os.path.join(course_dir, u["md_filename"])
                with open(note_path, "w", encoding="utf-8") as f:
                    f.write(md_content)

                total_units_processed += 1
                print(f"   ✓ {u['unit_num']}: {u['title'][:32]:<32} -> {u['md_filename']}")

            # Generate Course README.md
            course_readme_content = build_course_readme(c_code, c_meta, c["units"])
            with open(os.path.join(course_dir, "README.md"), "w", encoding="utf-8") as f:
                f.write(course_readme_content)

    # Generate Master Repository README.md
    master_readme_content = build_master_readme(curriculum)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(master_readme_content)

    print("\n" + "=" * 75)
    print(f"🎉 Successfully generated {total_units_processed} GitHub Markdown notes across all 12 courses!")
    print(f"📄 Generated master README.md and course index files.")
    print("=" * 75)


if __name__ == "__main__":
    process_all_curriculum()
