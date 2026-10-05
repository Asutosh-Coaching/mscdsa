#!/usr/bin/env python3
"""
mobile_reader_server.py
High-performance FastAPI web server powering the Lumina MSCDSA Mobile Study & Reader System.
Features:
- Mobile-first REST APIs for curriculum, units, notes, and study tracking
- Integrated Assignment Solutions viewer
- Local Wi-Fi network streaming for phone access (iOS / Android)
- Offline-capable Progressive Web App (PWA) static asset serving
"""

import os
import re
import json
import socket
from pathlib import Path
from typing import Optional, Dict, Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import mobile_reader.db as db

# Initialize FastAPI application
app = FastAPI(
    title="Lumina - MSCDSA Mobile Study & Reader",
    description="Mobile-optimized reading, comprehension, and completion system for IGNOU MSCDSA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_no_cache_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "mobile_reader" / "content"
STATIC_DIR = BASE_DIR / "mobile_reader" / "static"
CURRICULUM_PATH = BASE_DIR / "mobile_reader" / "curriculum.json"

# Ensure directories exist
os.makedirs(STATIC_DIR, exist_ok=True)


# Models
class ProgressUpdateRequest(BaseModel):
    course_code: str
    unit_id: str
    status: Optional[str] = None  # 'not_started', 'in_progress', 'completed'
    scroll_percent: Optional[float] = None
    last_page: Optional[int] = None
    added_seconds: int = 0


class NoteSaveRequest(BaseModel):
    note_content: str


def get_local_ip() -> str:
    """Finds the LAN IP address for easy mobile phone access over Wi-Fi."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


# --- API Routes ---

@app.get("/api/curriculum")
async def get_curriculum():
    """Returns the full curriculum tree enriched with user progress."""
    if not CURRICULUM_PATH.exists():
        raise HTTPException(status_code=500, detail="Curriculum manifest not found. Run build_mobile_library.py.")

    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    all_progress = db.get_all_progress()
    stats = db.get_study_stats()
    last_read = db.get_last_read_unit()

    # Enrich curriculum with live progress
    for sem_name, courses in curriculum["semesters"].items():
        for course in courses:
            c_code = course["code"]
            completed_in_course = 0
            for u in course["units"]:
                u_key = f"{c_code}::{u['unit_id']}"
                prog = all_progress.get(u_key, {})
                u["status"] = prog.get("status", "not_started")
                u["scroll_percent"] = prog.get("scroll_percent", 0.0)
                u["time_spent_seconds"] = prog.get("time_spent_seconds", 0)
                u["last_read_at"] = prog.get("last_read_at")
                if u["status"] == "completed":
                    completed_in_course += 1
            course["completed_units"] = completed_in_course
            course["completion_percentage"] = round((completed_in_course / max(1, course["total_units"])) * 100, 1)

    # Enrich last read unit details if present
    last_read_details = None
    if last_read:
        for sem_name, courses in curriculum["semesters"].items():
            for course in courses:
                if course["code"] == last_read["course_code"]:
                    for u in course["units"]:
                        if u["unit_id"] == last_read["unit_id"]:
                            last_read_details = {
                                "course_code": course["code"],
                                "course_title": course["title"],
                                "unit_id": u["unit_id"],
                                "unit_num": u["unit_num"],
                                "unit_title": u["title"],
                                "scroll_percent": last_read.get("scroll_percent", 0),
                                "time_spent_seconds": last_read.get("time_spent_seconds", 0)
                            }
                            break

    return {
        "curriculum": curriculum,
        "stats": stats,
        "last_read": last_read_details,
        "local_network_ip": get_local_ip()
    }


@app.get("/api/unit/{course_code}/{unit_id}")
async def get_unit(course_code: str, unit_id: str):
    """Returns the full unit content with objectives, text, flashcards, and navigation."""
    unit_path = CONTENT_DIR / course_code / f"{unit_id}.json"
    if not unit_path.exists():
        raise HTTPException(status_code=404, detail="Unit not found.")

    with open(unit_path, "r", encoding="utf-8") as f:
        unit_data = json.load(f)

    # Fetch notes and user progress
    user_note = db.get_note(course_code, unit_id)
    all_prog = db.get_all_progress()
    unit_key = f"{course_code}::{unit_id}"
    prog = all_prog.get(unit_key, {})

    unit_data["user_note"] = user_note
    unit_data["user_status"] = prog.get("status", "not_started")
    unit_data["user_scroll_percent"] = prog.get("scroll_percent", 0.0)
    unit_data["user_time_spent_seconds"] = prog.get("time_spent_seconds", 0)

    # Compute Previous and Next Unit pointers
    prev_unit = None
    next_unit = None
    if CURRICULUM_PATH.exists():
        with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
            curr = json.load(f)
        for sem, courses in curr["semesters"].items():
            for c in courses:
                if c["code"] == course_code:
                    units = c["units"]
                    for idx, u in enumerate(units):
                        if u["unit_id"] == unit_id:
                            if idx > 0:
                                prev_unit = {"unit_id": units[idx-1]["unit_id"], "title": units[idx-1]["title"], "unit_num": units[idx-1]["unit_num"]}
                            if idx < len(units) - 1:
                                next_unit = {"unit_id": units[idx+1]["unit_id"], "title": units[idx+1]["title"], "unit_num": units[idx+1]["unit_num"]}
                            break

    unit_data["prev_unit"] = prev_unit
    unit_data["next_unit"] = next_unit

    return unit_data


@app.post("/api/progress/update")
async def update_progress(req: ProgressUpdateRequest):
    """Updates reading progress or marks unit completed."""
    res = db.update_progress(
        course_code=req.course_code,
        unit_id=req.unit_id,
        status=req.status,
        scroll_percent=req.scroll_percent,
        last_page=req.last_page,
        added_seconds=req.added_seconds
    )
    stats = db.get_study_stats()
    return {"status": "ok", "result": res, "stats": stats}


@app.get("/api/notes/{course_code}/{unit_id}")
async def get_note(course_code: str, unit_id: str):
    """Retrieves personal study note for a unit."""
    note = db.get_note(course_code, unit_id)
    return {"course_code": course_code, "unit_id": unit_id, "note": note}


@app.post("/api/notes/{course_code}/{unit_id}")
async def save_note(course_code: str, unit_id: str, req: NoteSaveRequest):
    """Saves personal study note for a unit."""
    db.save_note(course_code, unit_id, req.note_content)
    return {"status": "saved", "course_code": course_code, "unit_id": unit_id}


@app.get("/api/stats")
async def get_stats():
    """Returns study streak, read minutes, and completion metrics."""
    return db.get_study_stats()


@app.get("/api/solution/{course_code}")
async def get_assignment_solution(course_code: str):
    """Retrieves the comprehensive assignment solution markdown for a course."""
    # Find matching solution file in assignment_solutions/
    solution_dir = BASE_DIR / "assignment_solutions"
    matching_files = list(solution_dir.glob(f"**/*{course_code}*.md"))

    if not matching_files:
        raise HTTPException(status_code=404, detail="Assignment solution not found for this course.")

    file_path = matching_files[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {
        "course_code": course_code,
        "filename": file_path.name,
        "markdown_content": content
    }


@app.get("/api/search")
async def search_library(q: str = Query(..., min_length=2)):
    """Fast search across course units, titles, and objectives."""
    if not CURRICULUM_PATH.exists():
        return []

    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    q_lower = q.lower().strip()
    results = []

    for sem_name, courses in curriculum["semesters"].items():
        for course in courses:
            c_code = course["code"]
            c_title = course["title"]
            for u in course["units"]:
                u_id = u["unit_id"]
                u_title = u["title"]
                score = 0
                match_reason = ""

                if q_lower in u_title.lower():
                    score += 10
                    match_reason = f"Title match: {u_title}"
                elif q_lower in c_title.lower():
                    score += 5
                    match_reason = f"Course: {c_title}"

                if score > 0:
                    results.append({
                        "course_code": c_code,
                        "course_title": c_title,
                        "unit_id": u_id,
                        "unit_num": u["unit_num"],
                        "title": u_title,
                        "score": score,
                        "match_reason": match_reason,
                        "est_read_time": u.get("est_read_time_minutes", 15)
                    })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:20]


@app.get("/pdf/{relative_path:path}")
async def serve_pdf(relative_path: str):
    """Serves original PDF files with byte-range support for mobile PDF viewing."""
    pdf_full_path = (BASE_DIR / relative_path).resolve()
    if not pdf_full_path.exists() or not str(pdf_full_path).startswith(str(BASE_DIR)):
        raise HTTPException(status_code=404, detail="PDF not found.")
    return FileResponse(pdf_full_path, media_type="application/pdf")


# Serve PWA manifest and service worker directly from root if requested
@app.get("/manifest.json")
async def get_manifest():
    return FileResponse(STATIC_DIR / "manifest.json", media_type="application/manifest+json")


@app.get("/sw.js")
async def get_sw():
    return FileResponse(STATIC_DIR / "sw.js", media_type="application/javascript")


# Mount static directory for JS, CSS, images
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_app(full_path: str):
    """Serves the Single-Page Application (SPA) shell."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        return HTMLResponse("<h1>Lumina Mobile Study & Reader</h1><p>Building app UI...</p>")
    with open(index_file, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


if __name__ == "__main__":
    import uvicorn
    local_ip = get_local_ip()
    print("=" * 65)
    print("  Lumina MSCDSA Mobile Study & Reader Server")
    print(f"  Local Desktop:  http://localhost:8000")
    print(f"  Mobile Phone:   http://{local_ip}:8000 (Connect on same Wi-Fi)")
    print("=" * 65)
    uvicorn.run(app, host="0.0.0.0", port=8000)
