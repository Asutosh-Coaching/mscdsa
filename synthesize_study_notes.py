#!/usr/bin/env python3
"""
synthesize_study_notes.py
Generates comprehensive, high-yield mobile study notes for all 112 IGNOU MSCDSA units.
Includes:
- Mermaid concept flowchart / pipeline
- Core definitions & terminology cards
- Structured important points topic-by-topic
- Formulas, algorithms, laws, and rules
- Interactive checkpoint flashcards
- Executive summary
- Collapsible full textbook text & direct link to original PDF
"""

import os
import re
import json
import sys
import fitz

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def sanitize_mermaid_label(text: str) -> str:
    """Cleans text for safe use inside Mermaid node labels."""
    clean = re.sub(r'["\(\)\[\]\{\}<>\n\r]', ' ', text).strip()
    return " ".join(clean.split())[:40]


def extract_structure_topics(full_text: str):
    """Extracts section numbering and titles from the Structure block or headings."""
    topics = []
    # Try Structure block first
    m = re.search(r'Structure\s*(.*?)(?=\n\s*(?:1\.0|\d+\.0)?\s*(?:INTRODUCTION|OBJECTIVES?))', full_text[:4000], re.DOTALL | re.IGNORECASE)
    if m:
        raw_topics = re.findall(r'(\d+\.\d+(?:\.\d+)?)\s*\n?\s*([A-Za-z][^\n\d]+)', m.group(1))
        for num, title in raw_topics:
            t = " ".join(title.split()).strip()
            if len(t) > 2 and not re.search(r'Further Readings|Solutions|Answers|References', t, re.IGNORECASE):
                topics.append((num, t))
                
    if not topics:
        # Fall back to finding section headers throughout text
        raw_headings = re.findall(r'\n(\d+\.\d+)\s+([A-Z][^\n]+)', full_text[:8000])
        for num, title in raw_headings:
            t = " ".join(title.split()).strip()
            if len(t) > 3 and not re.search(r'Further Readings|Solutions|Answers|References', t, re.IGNORECASE):
                topics.append((num, t))
                
    return topics


def generate_mermaid_flowchart(unit_num: str, unit_title: str, topics: list) -> str:
    """Generates a responsive Mermaid flowchart diagram from the unit topics."""
    clean_unit = sanitize_mermaid_label(f"{unit_num}: {unit_title}")
    
    # Filter major topics (e.g. 1.2, 1.3, not sub-sub topics)
    major_topics = [t for t in topics if t[0].count('.') == 1][:6]
    if not major_topics:
        major_topics = topics[:5]

    lines = ["graph TD"]
    lines.append(f'  Root["{clean_unit}"]')
    
    for idx, (num, title) in enumerate(major_topics, 1):
        node_id = f"N{idx}"
        clean_title = sanitize_mermaid_label(title)
        lines.append(f'  {node_id}["{num} {clean_title}"]')
        lines.append(f'  Root --> {node_id}')
        
        # Look for sub-topics under this major topic
        sub_topics = [t for t in topics if t[0].startswith(f"{num}.")][:3]
        for s_idx, (s_num, s_title) in enumerate(sub_topics, 1):
            sub_id = f"{node_id}_{s_idx}"
            clean_sub = sanitize_mermaid_label(s_title)
            lines.append(f'  {sub_id}["{clean_sub}"]')
            lines.append(f'  {node_id} --> {sub_id}')

    return "\n".join(lines)


def extract_definitions(full_text: str, topics: list) -> list:
    """Extracts key definitions and terminology from the unit text."""
    definitions = []
    
    # Pattern 1: Explicit definition patterns
    patterns = [
        r'(?:is\s+defined\s+as|may\s+be\s+defined\s+as|refers\s+to|is\s+known\s+as|means\s+that)\s+([^.\n]+(?:\.[^.\n]+)?)',
        r'Definition\s*(?:\d+(?:\.\d+)?)?\s*[:\-]?\s*([^.\n]+(?:\.[^.\n]+)?)'
    ]
    
    sentences = re.split(r'(?<=[.!?])\s+', full_text)
    
    for s in sentences:
        s_clean = " ".join(s.split()).strip()
        if len(s_clean) < 30 or len(s_clean) > 280:
            continue
            
        # Check if sentence contains definition indicator
        if re.search(r'\b(is defined as|is known as|refers to|can be defined as|Definition)\b', s_clean, re.IGNORECASE):
            # Extract concept term if possible
            term_match = re.match(r'^(?:A|An|The)?\s*([A-Za-z\s\-]{3,35})\s+(?:is|refers|can be)', s_clean, re.IGNORECASE)
            term = term_match.group(1).strip() if term_match else "Core Concept"
            
            # Avoid duplicate terms
            if not any(d['term'].lower() == term.lower() for d in definitions):
                definitions.append({
                    "term": term.title(),
                    "definition": s_clean,
                    "category": "Definition"
                })
                if len(definitions) >= 6:
                    break
                    
    # If fewer than 4 definitions found, supplement from major topic titles
    if len(definitions) < 4 and topics:
        for num, title in topics[:6]:
            if not any(d['term'].lower() in title.lower() for d in definitions):
                # Search for first sentence mentioning this topic
                for s in sentences:
                    if title.lower() in s.lower() and len(s) > 35 and len(s) < 250:
                        definitions.append({
                            "term": title.title(),
                            "definition": " ".join(s.split()).strip(),
                            "category": "Key Topic"
                        })
                        break
            if len(definitions) >= 6:
                break
                
    return definitions[:6]


def extract_important_points(full_text: str, topics: list) -> list:
    """Extracts organized important points and exam takeaways topic by topic."""
    sections_notes = []
    
    # Process top 4-6 major topics
    major_topics = [t for t in topics if t[0].count('.') <= 2][:6]
    if not major_topics:
        # Fall back to generic paragraph extraction
        paragraphs = [p.strip() for p in full_text.split('\n\n') if len(p.strip()) > 100 and len(p.strip()) < 500]
        pts = [" ".join(p.split()) for p in paragraphs[:5]]
        return [{"topic": "Key Principles", "points": pts}]

    for num, title in major_topics:
        # Search for text chunk around this section
        sec_regex = re.escape(num) + r'\s+' + re.escape(title[:15])
        m = re.search(sec_regex, full_text, re.IGNORECASE)
        points = []
        if m:
            start_pos = m.start()
            chunk = full_text[start_pos:start_pos+3500]
            # Extract informative sentences
            raw_sents = re.split(r'(?<=[.!?])\s+', chunk)
            for sent in raw_sents[1:]:
                sent_clean = " ".join(sent.split()).strip()
                if len(sent_clean) > 40 and len(sent_clean) < 220:
                    if not re.search(r'fig|table|chapter|unit|check your progress|we will learn|exercise', sent_clean, re.IGNORECASE):
                        points.append(sent_clean)
                if len(points) >= 3:
                    break
                    
        if not points:
            points = [f"Focuses on foundational theoretical principles, operational definitions, and methods of {title.lower()}."]

        sections_notes.append({
            "section_num": num,
            "topic": title,
            "points": points[:3]
        })
        
    return sections_notes


def extract_formulas_and_rules(full_text: str) -> list:
    """Extracts mathematical formulas, algebraic equations, laws, and rules."""
    formulas = []
    
    # Look for math equations, laws, or theorems
    laws_matches = re.finditer(r'(?:Law|Theorem|Property|Rule|Formula)\s*(?:\d+(?:\.\d+)?)?\s*[:\-]?\s*([^\n\.]+(?:\.[^\n\.]+)*)', full_text, re.IGNORECASE)
    for m in laws_matches:
        f_text = " ".join(m.group(0).split()).strip()
        if len(f_text) > 20 and len(f_text) < 220:
            formulas.append(f_text)
        if len(formulas) >= 4:
            break
            
    # Look for bullet points with math / code / arrows
    if len(formulas) < 3:
        math_sents = [s.strip() for s in full_text.split('\n') if re.search(r'[=<>≤≥∪∩∈⊆∑∏λμβσα]|\b(?:O\(|select\s+|def\s+|return\s+)\b', s, re.IGNORECASE)]
        for ms in math_sents:
            clean_ms = " ".join(ms.split()).strip()
            if len(clean_ms) > 15 and len(clean_ms) < 160:
                formulas.append(clean_ms)
            if len(formulas) >= 4:
                break
                
    return formulas[:4]


def extract_flashcards(full_text: str, objectives: list, definitions: list) -> list:
    """Extracts or synthesizes high-yield Q&A flashcards for self-testing."""
    flashcards = []
    
    # 1. Look for Check Your Progress questions
    cyp_matches = list(re.finditer(r'(?:Check\s+Your\s+Progress\s*(\d*)|CYP\s*(\d*))\s*(.*?)(?=\n\s*(?:Check\s+Your\s+Progress|\d+\.\d+|SUMMARY|ANSWERS|$))', full_text, re.DOTALL | re.IGNORECASE))
    for m in cyp_matches[:4]:
        block = m.group(3).strip()
        sub_qs = re.findall(r'(?:(\d+)\.\s*|\(\w+\)\s*)([^\n]+(?:\n[^\d\n•]+)*)', block)
        for num, q_text in sub_qs[:2]:
            q_clean = " ".join(q_text.split()).strip()
            if len(q_clean) > 20 and len(q_clean) < 220:
                flashcards.append({
                    "question": q_clean,
                    "answer": "Refer to the corresponding unit section and formula card for step-by-step verification.",
                    "tag": "CYP Exercise"
                })
                
    # 2. Add definitions as flashcards
    for d in definitions[:3]:
        flashcards.append({
            "question": f"What is the formal definition and significance of {d['term']}?",
            "answer": d['definition'],
            "tag": "Key Term"
        })
        
    # 3. Add objectives as flashcards
    for obj in objectives[:3]:
        clean_obj = obj.strip()
        if len(clean_obj) > 15:
            flashcards.append({
                "question": f"Review Checkpoint: How do you {clean_obj[0].lower() + clean_obj[1:]}?",
                "answer": f"Core takeaway from unit learning objectives: Master {clean_obj}.",
                "tag": "Learning Objective"
            })
            
    return flashcards[:8]


def build_notes_html(unit_num: str, unit_title: str, flowchart: str,
                     definitions: list, important_points: list,
                     formulas: list, summary: str, total_pages: int,
                     relative_pdf: str, raw_html: str) -> str:
    """
    Renders high-yield study notes with visual flowchart, definition cards,
    topic breakdowns, formulas, summary, and a collapsible full textbook accordion.
    """
    html = []
    
    # 1. Visual Flowchart Card
    html.append(f'''
    <div class="study-card flowchart-card">
      <div class="study-card-header">
        <span class="study-card-badge">🗺️ Concept Map & Hierarchy</span>
        <h3 class="study-card-title">Unit Architecture Flowchart</h3>
      </div>
      <div class="mermaid-diagram-box">
        <pre class="mermaid">
{flowchart}
        </pre>
      </div>
    </div>
    ''')

    # 2. Core Definitions & Terminology
    if definitions:
        html.append('''
        <div class="study-card">
          <div class="study-card-header">
            <span class="study-card-badge">📖 Core Definitions</span>
            <h3 class="study-card-title">Essential Terminology & Concepts</h3>
          </div>
          <div class="definitions-grid">
        ''')
        for d in definitions:
            html.append(f'''
            <div class="def-card">
              <div class="def-header">
                <span class="def-term">{d['term']}</span>
                <span class="def-tag">{d.get('category', 'Definition')}</span>
              </div>
              <p class="def-text">{d['definition']}</p>
            </div>
            ''')
        html.append('</div></div>')

    # 3. Important Points Topic-by-Topic
    if important_points:
        html.append('''
        <div class="study-card">
          <div class="study-card-header">
            <span class="study-card-badge">📌 Key Takeaways</span>
            <h3 class="study-card-title">Structured Topic Summary</h3>
          </div>
          <div class="topics-summary-list">
        ''')
        for sec in important_points:
            html.append(f'''
            <div class="topic-item">
              <h4 class="topic-item-title">{sec.get('section_num', '')} {sec['topic']}</h4>
              <ul class="topic-item-bullets">
            ''')
            for pt in sec['points']:
                html.append(f'<li>{pt}</li>')
            html.append('</ul></div>')
        html.append('</div></div>')

    # 4. Formulas, Laws & Rules
    if formulas:
        html.append('''
        <div class="study-card formulas-card">
          <div class="study-card-header">
            <span class="study-card-badge">⚡ Laws & Formulas</span>
            <h3 class="study-card-title">Governing Equations, Properties & Rules</h3>
          </div>
          <div class="formulas-list">
        ''')
        for f in formulas:
            html.append(f'<div class="formula-box"><code>{f}</code></div>')
        html.append('</div></div>')

    # 5. Executive Summary
    if summary:
        html.append(f'''
        <div class="study-card summary-card">
          <div class="study-card-header">
            <span class="study-card-badge">🎯 Unit Summary</span>
            <h3 class="study-card-title">High-Impact Wrap-Up</h3>
          </div>
          <p class="summary-text">{summary}</p>
        </div>
        ''')

    # 6. Full Textbook / PDF Toggle Section
    html.append(f'''
    <div class="study-card pdf-switch-card">
      <div class="study-card-header">
        <span class="study-card-badge">📚 Deep Dive</span>
        <h3 class="study-card-title">Need the Unabridged 30-40 Page Textbook?</h3>
      </div>
      <p class="reader-p" style="margin-bottom:14px; font-size:14px; color:var(--text-secondary);">
        You have completed the high-yield study notes. If you want to consult original formulas, detailed historical background, or diagrams:
      </p>
      <div style="display:flex; flex-direction:column; gap:10px;">
        <button class="btn-primary" style="background:var(--primary); width:100%;" onclick="togglePdfView('{relative_pdf}')">
          📄 Read Original IGNOU PDF ({total_pages} Pages)
        </button>
        <button class="btn-primary" style="background:var(--bg-card); color:var(--text-primary); border:1px solid var(--border-color); width:100%;" onclick="toggleRawText()">
          📖 Expand Full Extracted Text Stream
        </button>
      </div>
      
      <!-- Collapsible Full Text Container -->
      <div id="raw-text-accordion" style="display:none; margin-top:16px; border-top:1px dashed var(--border-color); padding-top:16px;">
        <div style="font-size:12px; color:var(--text-muted); margin-bottom:12px;">Full Unabridged Raw Text:</div>
        {raw_html}
      </div>
    </div>
    ''')

    return "\n".join(html)


def process_all_units():
    print("=" * 70)
    print("🧠 Synthesizing High-Yield Study Notes for All 112 Units")
    print("=" * 70)
    
    content_base = os.path.join("mobile_reader", "content")
    courses = sorted(os.listdir(content_base))
    
    total_processed = 0
    
    for c_code in courses:
        c_dir = os.path.join(content_base, c_code)
        if not os.path.isdir(c_dir):
            continue
            
        unit_files = sorted([f for f in os.listdir(c_dir) if f.endswith('.json')])
        print(f"\n📂 [{c_code}] Processing {len(unit_files)} modules...")
        
        for u_file in unit_files:
            u_path = os.path.join(c_dir, u_file)
            with open(u_path, "r", encoding="utf-8") as f:
                unit = json.load(f)
                
            pdf_rel = unit.get("relative_pdf_path", "")
            if not os.path.exists(pdf_rel):
                continue
                
            doc = fitz.open(pdf_rel)
            pages_text = [p.get_text() for p in doc]
            full_text = "\n".join(pages_text)
            doc.close()
            
            # 1. Extract Structure Topics
            topics = extract_structure_topics(full_text)
            
            # 2. Generate Flowchart
            flowchart = generate_mermaid_flowchart(unit["unit_num"], unit["title"], topics)
            
            # 3. Extract Definitions
            definitions = extract_definitions(full_text, topics)
            
            # 4. Extract Important Points
            important_points = extract_important_points(full_text, topics)
            
            # 5. Extract Formulas & Rules
            formulas = extract_formulas_and_rules(full_text)
            
            # 6. Extract Flashcards
            flashcards = extract_flashcards(full_text, unit.get("objectives", []), definitions)
            
            # 7. Extract Summary if missing
            summary = unit.get("summary", "")
            if not summary or len(summary) < 50:
                sum_match = re.search(r'(?:SUMMARY|1\.\d+\s+SUMMARY)\s*(.*?)(?=\n\s*(?:ANSWERS|SOLUTIONS|REFERENCES|$))', full_text, re.DOTALL | re.IGNORECASE)
                if sum_match:
                    s_lines = [l.strip() for l in sum_match.group(1).split('\n') if len(l.strip()) > 20]
                    summary = " ".join(s_lines[:8])
                else:
                    summary = f"This unit establishes foundational theoretical competencies, analytical methodologies, and practical applications in {unit['title']}."

            # 8. Render Study Notes HTML Layout
            study_notes_html = build_notes_html(
                unit_num=unit["unit_num"],
                unit_title=unit["title"],
                flowchart=flowchart,
                definitions=definitions,
                important_points=important_points,
                formulas=formulas,
                summary=summary,
                total_pages=unit["total_pages"],
                relative_pdf=pdf_rel,
                raw_html=unit.get("html_content", "")
            )
            
            # Update Unit JSON
            unit["flowchart_mermaid"] = flowchart
            unit["definitions"] = definitions
            unit["important_points"] = important_points
            unit["formulas"] = formulas
            unit["flashcards"] = flashcards
            unit["summary"] = summary
            unit["study_notes_html"] = study_notes_html
            
            # Write back
            with open(u_path, "w", encoding="utf-8") as f:
                json.dump(unit, f, ensure_ascii=False, indent=2)
                
            total_processed += 1
            print(f"   ✓ {unit['unit_num']}: {unit['title'][:32]:<32} (Flowchart, {len(definitions)} Defs, {len(flashcards)} Flashcards)")

    print("\n" + "=" * 70)
    print(f"🎉 Successfully synthesized High-Yield Study Notes for {total_processed} Units!")
    print("=" * 70)


if __name__ == "__main__":
    process_all_units()
