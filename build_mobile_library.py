#!/usr/bin/env python3
"""
build_mobile_library.py
Extracts and structures all IGNOU MSCDSA course books into mobile-optimized
reading modules with objectives, clean reflowable text, flashcards, and metadata.
"""

import os
import re
import json
import sys
import fitz  # PyMuPDF

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

COURSE_METADATA = {
    # Semester 1
    "MCS-061": {
        "title": "Mathematical Foundations - I",
        "semester": 1,
        "credits": 4,
        "type": "Theory",
        "description": "Linear Algebra, Matrices, Determinants, Vector Spaces, Calculus, and Counting Techniques.",
        "solution_file": "assignment_solutions/Semester_1/MCS-061_Mathematical_Foundations_I_Assignment_Solutions.md"
    },
    "MCS-062": {
        "title": "Introduction to Data Science",
        "semester": 1,
        "credits": 4,
        "type": "Theory",
        "description": "Data Science Lifecycle, Data Preparation, EDA, Big Data, NoSQL, and Analytical Tools.",
        "solution_file": "assignment_solutions/Semester_1/MCS-062_Introduction_to_Data_Science_Assignment_Solutions.md"
    },
    "MCS-063": {
        "title": "Data Structures using Python",
        "semester": 1,
        "credits": 4,
        "type": "Theory",
        "description": "Python OOP, Recursion, Trees, Graphs, Sorting, Heaps, and Algorithm Complexity.",
        "solution_file": "assignment_solutions/Semester_1/MCS-063_Data_Structures_using_Python_Assignment_Solutions.md"
    },
    "MCS-207": {
        "title": "Database Management Systems",
        "semester": 1,
        "credits": 4,
        "type": "Theory",
        "description": "Relational Models, SQL, Normalization, ACID Transactions, Concurrency, and NoSQL.",
        "solution_file": "assignment_solutions/Semester_1/MCS-207_Database_Management_Systems_Assignment_Solutions.md"
    },
    "MCSL-064": {
        "title": "Data Structures using Python Lab",
        "semester": 1,
        "credits": 2,
        "type": "Practical",
        "description": "Hands-on implementations of Python data structures, ADTs, search and sort algorithms.",
        "solution_file": "assignment_solutions/Semester_1/MCSL-064_Data_Structures_using_Python_Lab_Assignment_Solutions.md"
    },
    "MCSL-065": {
        "title": "Data Science Lab",
        "semester": 1,
        "credits": 2,
        "type": "Practical",
        "description": "Applied Data Science pipelines using Excel, Tableau, Power BI, Python, and R.",
        "solution_file": "assignment_solutions/Semester_1/MCSL-065_Data_Science_Lab_Assignment_Solutions.md"
    },
    # Semester 2
    "MCS-066": {
        "title": "Mathematical Foundations - II",
        "semester": 2,
        "credits": 4,
        "type": "Theory",
        "description": "Probability, Distributions, Central Limit Theorem, Hypothesis Testing, ANOVA, and Chi-Square.",
        "solution_file": "assignment_solutions/Semester_2/MCS-066_Mathematical_Foundations_II_Assignment_Solutions.md"
    },
    "MCS-067": {
        "title": "Data Wrangling and Visualization",
        "semester": 2,
        "credits": 4,
        "type": "Theory",
        "description": "Data Cleaning, MultiIndex Reshaping, Matplotlib/Seaborn Dashboards, and Trellis Paradigm.",
        "solution_file": "assignment_solutions/Semester_2/MCS-067_Data_Wrangling_and_Visualization_Assignment_Solutions.md"
    },
    "MCS-068": {
        "title": "Predictive Data Analysis",
        "semester": 2,
        "credits": 4,
        "type": "Theory",
        "description": "Time Series (ARIMA), Linear Programming, Regression, KNN, K-Means, and Jaccard Similarity.",
        "solution_file": "assignment_solutions/Semester_2/MCS-068_Predictive_Data_Analysis_Assignment_Solutions.md"
    },
    "MCS-224": {
        "title": "Artificial Intelligence & Machine Learning",
        "semester": 2,
        "credits": 4,
        "type": "Theory",
        "description": "Search Algorithms, Fuzzy Logic, Decision Trees (ID3), SVM, Neural Networks, PCA, and Apriori.",
        "solution_file": "assignment_solutions/Semester_2/MCS-224_Artificial_Intelligence_and_Machine_Learning_Assignment_Solutions.md"
    },
    "MCSL-069": {
        "title": "AI & Machine Learning Lab",
        "semester": 2,
        "credits": 2,
        "type": "Practical",
        "description": "Python implementations of N-Queens, Water Jug, Minimax, AO*, Naive Bayes, ID3, and SVM.",
        "solution_file": "assignment_solutions/Semester_2/MCSL-069_Artificial_Intelligence_and_Machine_Learning_Lab_Assignment_Solutions.md"
    },
    "MCSL-070": {
        "title": "Data Analysis Lab",
        "semester": 2,
        "credits": 2,
        "type": "Practical",
        "description": "Data wrangling in Python and advanced statistical modeling and machine learning in R.",
        "solution_file": "assignment_solutions/Semester_2/MCSL-070_Data_Analysis_Lab_Assignment_Solutions.md"
    }
}


def clean_text_segment(text: str) -> str:
    """Removes annoying PDF headers, footers, and page numbers."""
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        # Drop standalone page numbers (e.g., '1', '23', 'Page 12')
        if re.match(r"^(Page\s+)?\d{1,4}$", stripped, re.IGNORECASE):
            continue
        # Drop common IGNOU running headers
        if re.search(r"Indira Gandhi National Open University|School of Computer and Information Sciences", stripped, re.IGNORECASE):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines).strip()


def parse_unit_structure(full_text: str):
    """
    Parses objectives, key concepts, check-your-progress questions,
    and sections from raw unit text.
    """
    # 1. Extract Objectives
    objectives = []
    obj_match = re.search(r"(?:1\.0\s+)?OBJECTIVES?\s*(.*?)(?=\n\s*(?:1\.1|\d+\.1|INTRODUCTION|Structure|$))", full_text, re.DOTALL | re.IGNORECASE)
    if obj_match:
        obj_text = obj_match.group(1).strip()
        # Look for bullet points or bullet lines
        bullets = re.findall(r"(?:[•\-\*]\s*|\(\w+\)\s*|[a-z]\)\s*)([^\n•\-\*]+)", obj_text)
        if bullets:
            objectives = [b.strip() for b in bullets if len(b.strip()) > 8][:6]
        else:
            lines = [l.strip() for l in obj_text.split("\n") if len(l.strip()) > 15]
            objectives = lines[:5]

    # 2. Extract Check Your Progress (CYP) flashcards
    flashcards = []
    cyp_matches = list(re.finditer(r"(?:Check\s+Your\s+Progress\s*(\d*)|CYP\s*(\d*))\s*(.*?)(?=\n\s*(?:Check\s+Your\s+Progress|\d+\.\d+|SUMMARY|ANSWERS|$))", full_text, re.DOTALL | re.IGNORECASE))
    for m in cyp_matches[:4]:
        block = m.group(3).strip()
        # Split into numbered sub-questions
        sub_qs = re.findall(r"(?:(\d+)\.\s*|\(\w+\)\s*)([^\n]+(?:\n[^\d\n•]+)*)", block)
        for num, q_text in sub_qs[:3]:
            q_clean = " ".join(q_text.split()).strip()
            if len(q_clean) > 15:
                flashcards.append({
                    "question": q_clean,
                    "hint": "Check the corresponding unit section for detailed explanation and answers."
                })

    # If no explicit CYP questions matched, create high-yield concept review questions from objectives
    if not flashcards and objectives:
        for obj in objectives[:4]:
            flashcards.append({
                "question": f"Key Checkpoint: Explain how to {obj.lower()}",
                "hint": f"Review section relevant to: {obj}"
            })

    # 3. Extract Summary if available
    summary = ""
    summary_match = re.search(r"(?:SUMMARY|1\.\d+\s+SUMMARY)\s*(.*?)(?=\n\s*(?:ANSWERS|SOLUTIONS|REFERENCES|FURTHER READINGS|$))", full_text, re.DOTALL | re.IGNORECASE)
    if summary_match:
        s_lines = [l.strip() for l in summary_match.group(1).split("\n") if len(l.strip()) > 20]
        summary = " ".join(s_lines[:10])

    return objectives, flashcards, summary


def format_html_content(pages_text: list) -> str:
    """
    Transforms extracted pages into clean, responsive HTML with section headers,
    readable paragraphs, callout boxes, and syntax highlights.
    """
    html_parts = []
    
    for page_idx, raw_page in enumerate(pages_text, 1):
        cleaned = clean_text_segment(raw_page)
        if not cleaned:
            continue
            
        paragraphs = cleaned.split("\n\n")
        page_html = [f'<div class="reader-page-break" data-page="{page_idx}"><span>Page {page_idx}</span></div>']
        
        for p in paragraphs:
            p_strip = p.strip()
            if not p_strip:
                continue
                
            # Check for major Section Header (e.g., '1.2 Sets', '2.3 Types of Progressions')
            if re.match(r"^\d+\.\d+(\.\d+)?\s+[A-Z]", p_strip) and len(p_strip.split("\n")[0]) < 80:
                header_line = p_strip.split("\n")[0]
                rest = "\n".join(p_strip.split("\n")[1:])
                page_html.append(f'<h3 class="reader-heading">{header_line}</h3>')
                if rest.strip():
                    page_html.append(f'<p class="reader-p">{rest.strip()}</p>')
            # Check for Objectives / Summary / CYP headers
            elif re.match(r"^(OBJECTIVES?|SUMMARY|INTRODUCTION|CHECK YOUR PROGRESS)", p_strip, re.IGNORECASE):
                lines = p_strip.split("\n")
                page_html.append(f'<h2 class="reader-subheading">{lines[0]}</h2>')
                if len(lines) > 1:
                    page_html.append(f'<p class="reader-p">{"<br>".join(lines[1:])}</p>')
            # Check for Key Formula or Definition callout
            elif re.search(r"^(Definition|Theorem|Formula|Example\s+\d+|Note:)", p_strip, re.IGNORECASE):
                page_html.append(f'<div class="reader-callout"><div class="callout-badge">Key Concept</div><p>{p_strip}</p></div>')
            else:
                formatted_p = " ".join(p_strip.split())
                # Highlight bold concepts
                formatted_p = re.sub(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+is\s+defined\s+as)", r"<strong>\1</strong>", formatted_p)
                page_html.append(f'<p class="reader-p">{formatted_p}</p>')
                
        html_parts.append("\n".join(page_html))
        
    return "\n".join(html_parts)


def process_course_folder(sem_dir: str, course_folder: str, course_code: str):
    """Processes all unit PDFs in a course directory."""
    course_path = os.path.join(sem_dir, course_folder)
    out_dir = os.path.join("mobile_reader", "content", course_code)
    os.makedirs(out_dir, exist_ok=True)
    
    # Identify all PDF files in this folder
    all_pdfs = [f for f in os.listdir(course_path) if f.endswith(".pdf")]
    
    # Filter unit/reading PDFs: prefer Unit-*, Section-*, or standalone lab manual
    unit_pdfs = [f for f in all_pdfs if f.startswith("Unit-") or f.startswith("Section-")]
    if not unit_pdfs:
        # Fall back to non-assignment, non-block PDFs
        unit_pdfs = [f for f in all_pdfs if "Assign" not in f and not f.startswith("Block-")]
    if not unit_pdfs:
        # If still none, use Block PDFs
        unit_pdfs = [f for f in all_pdfs if "Assign" not in f]

    # Sort naturally by Unit number
    def sort_key(fn):
        m = re.search(r"(?:Unit|Section)[-_](\d+)", fn, re.IGNORECASE)
        return int(m.group(1)) if m else 999
    unit_pdfs.sort(key=sort_key)
    
    units_manifest = []
    
    for idx, pdf_name in enumerate(unit_pdfs, 1):
        pdf_path = os.path.join(course_path, pdf_name)
        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
            pages_text = [page.get_text() for page in doc]
            full_text = "\n".join(pages_text)
            
            # Extract Unit Number and Title from filename or first page
            unit_id = f"unit_{idx:02d}"
            # Extract clean title from filename
            clean_title = re.sub(r"^(?:Unit|Section)[-_]\d+[-_]", "", pdf_name[:-4])
            clean_title = clean_title.replace("_", " ").strip()
            if not clean_title or clean_title.isdigit():
                clean_title = f"Module {idx}"
                
            unit_display_num = f"Unit {idx}" if "Unit" in pdf_name else f"Section {idx}"
            
            # Parse structure: Objectives, Flashcards, Summary
            objectives, flashcards, summary = parse_unit_structure(full_text)
            
            # Format HTML
            html_content = format_html_content(pages_text)
            
            # Word count and read time
            word_count = len(full_text.split())
            read_time_min = max(8, round(word_count / 180)) # 180 wpm
            
            unit_data = {
                "course_code": course_code,
                "unit_id": unit_id,
                "unit_num": unit_display_num,
                "title": clean_title,
                "filename": pdf_name,
                "relative_pdf_path": os.path.relpath(pdf_path, ".").replace("\\", "/"),
                "total_pages": total_pages,
                "word_count": word_count,
                "est_read_time_minutes": read_time_min,
                "objectives": objectives,
                "summary": summary,
                "flashcards": flashcards,
                "html_content": html_content
            }
            
            # Save unit JSON
            unit_json_path = os.path.join(out_dir, f"{unit_id}.json")
            with open(unit_json_path, "w", encoding="utf-8") as f:
                json.dump(unit_data, f, ensure_ascii=False, indent=2)
                
            # Add to manifest (compact without large html)
            units_manifest.append({
                "unit_id": unit_id,
                "unit_num": unit_display_num,
                "title": clean_title,
                "filename": pdf_name,
                "total_pages": total_pages,
                "est_read_time_minutes": read_time_min,
                "objectives_count": len(objectives),
                "flashcards_count": len(flashcards),
                "has_summary": bool(summary)
            })
            
            doc.close()
            print(f"    ✓ {unit_display_num}: {clean_title[:35]:<35} ({total_pages} pages, ~{read_time_min}m read)")
            
        except Exception as e:
            print(f"    ✗ Error processing {pdf_name}: {e}")
            
    return units_manifest


def main():
    print("=" * 70)
    print("🚀 Building Mobile Study & Reader Library for IGNOU MSCDSA")
    print("=" * 70)
    
    curriculum = {
        "program": "M.Sc. (Data Science and Analytics) (MSCDSA)",
        "university": "IGNOU SOCIS",
        "semesters": {
            "Semester_1": [],
            "Semester_2": []
        }
    }
    
    total_units_count = 0
    total_pages_count = 0
    
    for sem_name, sem_num in [("Semester_1", 1), ("Semester_2", 2)]:
        sem_dir = os.path.join("pdfs", sem_name)
        if not os.path.exists(sem_dir):
            continue
            
        print(f"\n📂 Processing {sem_name}...")
        course_folders = sorted(os.listdir(sem_dir))
        
        for folder in course_folders:
            folder_path = os.path.join(sem_dir, folder)
            if not os.path.isdir(folder_path):
                continue
                
            # Extract course code (e.g., MCS-061)
            m = re.match(r"(MCSL?-\d+)", folder)
            course_code = m.group(1) if m else folder
            
            meta = COURSE_METADATA.get(course_code, {
                "title": folder.replace("_", " "),
                "semester": sem_num,
                "credits": 4,
                "type": "Theory",
                "description": "",
                "solution_file": ""
            })
            
            print(f"  📖 [{course_code}] {meta['title']} ({meta['credits']} Credits)")
            units = process_course_folder(sem_dir, folder, course_code)
            
            course_entry = {
                "code": course_code,
                "folder": folder,
                "title": meta["title"],
                "semester": meta["semester"],
                "credits": meta["credits"],
                "type": meta["type"],
                "description": meta["description"],
                "solution_file": meta["solution_file"],
                "total_units": len(units),
                "total_pages": sum(u["total_pages"] for u in units),
                "total_read_time_minutes": sum(u["est_read_time_minutes"] for u in units),
                "units": units
            }
            
            curriculum["semesters"][sem_name].append(course_entry)
            total_units_count += len(units)
            total_pages_count += course_entry["total_pages"]
            
    # Save master curriculum manifest
    manifest_path = os.path.join("mobile_reader", "curriculum.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
        
    print("\n" + "=" * 70)
    print(f"🎉 Library Build Complete!")
    print(f"   Total Units Processed: {total_units_count}")
    print(f"   Total Pages Processed: {total_pages_count}")
    print(f"   Curriculum Manifest Saved to: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
