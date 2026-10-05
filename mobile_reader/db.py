#!/usr/bin/env python3
"""
db.py
SQLite database manager for tracking user reading progress, unit completion,
bookmarks, personal notes, study streaks, and active learning checkpoints.
"""

import sqlite3
import os
import datetime
from typing import Dict, List, Optional, Any

DB_PATH = os.path.join("mobile_reader", "study_data.db")


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes database tables if they do not exist."""
    os.makedirs("mobile_reader", exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Reading Progress Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reading_progress (
        course_code TEXT NOT NULL,
        unit_id TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'not_started', -- 'not_started', 'in_progress', 'completed'
        scroll_percent REAL DEFAULT 0.0,
        last_page INTEGER DEFAULT 1,
        time_spent_seconds INTEGER DEFAULT 0,
        completed_at TIMESTAMP,
        last_read_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (course_code, unit_id)
    )
    """)

    # 2. Personal Notes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS unit_notes (
        course_code TEXT NOT NULL,
        unit_id TEXT NOT NULL,
        note_content TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (course_code, unit_id)
    )
    """)

    # 3. Bookmarks Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT NOT NULL,
        unit_id TEXT NOT NULL,
        title TEXT NOT NULL,
        snippet TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 4. Daily Study Log Table (for streaks and analytics)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_study_log (
        study_date DATE PRIMARY KEY,
        seconds_read INTEGER DEFAULT 0,
        units_completed INTEGER DEFAULT 0
    )
    """)

    # 5. User Settings Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_settings (
        setting_key TEXT PRIMARY KEY,
        setting_val TEXT
    )
    """)

    # Default daily goal: 1 unit per day, 30 mins
    cursor.execute("""
    INSERT OR IGNORE INTO user_settings (setting_key, setting_val)
    VALUES ('daily_goal_units', '1'), ('daily_goal_minutes', '30'), ('theme', 'sepia'), ('font_size', '18')
    """)

    conn.commit()
    conn.close()


def update_progress(course_code: str, unit_id: str, status: Optional[str] = None,
                    scroll_percent: Optional[float] = None, last_page: Optional[int] = None,
                    added_seconds: int = 0) -> Dict[str, Any]:
    """Updates or inserts reading progress for a unit."""
    conn = get_db_connection()
    cursor = conn.cursor()

    now = datetime.datetime.now().isoformat()
    today = datetime.date.today().isoformat()

    # Get current record
    cursor.execute("SELECT * FROM reading_progress WHERE course_code = ? AND unit_id = ?",
                   (course_code, unit_id))
    row = cursor.fetchone()

    is_newly_completed = False

    if row is None:
        curr_status = status or 'in_progress'
        curr_scroll = scroll_percent or 0.0
        curr_page = last_page or 1
        curr_time = added_seconds
        completed_at = now if curr_status == 'completed' else None
        if curr_status == 'completed':
            is_newly_completed = True

        cursor.execute("""
        INSERT INTO reading_progress (course_code, unit_id, status, scroll_percent, last_page, time_spent_seconds, completed_at, last_read_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (course_code, unit_id, curr_status, curr_scroll, curr_page, curr_time, completed_at, now))
    else:
        new_status = status if status is not None else row['status']
        new_scroll = scroll_percent if scroll_percent is not None else row['scroll_percent']
        new_page = last_page if last_page is not None else row['last_page']
        new_time = row['time_spent_seconds'] + added_seconds

        completed_at = row['completed_at']
        if new_status == 'completed' and row['status'] != 'completed':
            completed_at = now
            is_newly_completed = True
        elif new_status != 'completed':
            completed_at = None

        cursor.execute("""
        UPDATE reading_progress
        SET status = ?, scroll_percent = ?, last_page = ?, time_spent_seconds = ?, completed_at = ?, last_read_at = ?
        WHERE course_code = ? AND unit_id = ?
        """, (new_status, new_scroll, new_page, new_time, completed_at, now, course_code, unit_id))

    # Update Daily Log
    cursor.execute("INSERT OR IGNORE INTO daily_study_log (study_date, seconds_read, units_completed) VALUES (?, 0, 0)", (today,))
    units_inc = 1 if is_newly_completed else 0
    cursor.execute("""
    UPDATE daily_study_log
    SET seconds_read = seconds_read + ?, units_completed = units_completed + ?
    WHERE study_date = ?
    """, (added_seconds, units_inc, today))

    conn.commit()
    conn.close()

    return {"course_code": course_code, "unit_id": unit_id, "status": status, "is_newly_completed": is_newly_completed}


def get_all_progress() -> Dict[str, Dict[str, Any]]:
    """Returns a lookup dictionary of all tracked unit progress."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reading_progress")
    rows = cursor.fetchall()
    conn.close()

    progress = {}
    for r in rows:
        key = f"{r['course_code']}::{r['unit_id']}"
        progress[key] = {
            "course_code": r['course_code'],
            "unit_id": r['unit_id'],
            "status": r['status'],
            "scroll_percent": r['scroll_percent'],
            "last_page": r['last_page'],
            "time_spent_seconds": r['time_spent_seconds'],
            "completed_at": r['completed_at'],
            "last_read_at": r['last_read_at']
        }
    return progress


def get_last_read_unit() -> Optional[Dict[str, Any]]:
    """Returns the most recently accessed unit to power the 'Resume Reading' card."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM reading_progress
    ORDER BY last_read_at DESC
    LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_study_stats() -> Dict[str, Any]:
    """Calculates overall completion metrics, study streak, and daily progress."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Total units completed
    cursor.execute("SELECT COUNT(*) FROM reading_progress WHERE status = 'completed'")
    completed_units = cursor.fetchone()[0]

    # Total units in progress
    cursor.execute("SELECT COUNT(*) FROM reading_progress WHERE status = 'in_progress'")
    in_progress_units = cursor.fetchone()[0]

    # Total reading time
    cursor.execute("SELECT SUM(time_spent_seconds) FROM reading_progress")
    total_seconds = cursor.fetchone()[0] or 0

    # Today's study time and units
    today = datetime.date.today().isoformat()
    cursor.execute("SELECT seconds_read, units_completed FROM daily_study_log WHERE study_date = ?", (today,))
    today_row = cursor.fetchone()
    today_seconds = today_row['seconds_read'] if today_row else 0
    today_units = today_row['units_completed'] if today_row else 0

    # Calculate streak (consecutive active days)
    cursor.execute("SELECT study_date FROM daily_study_log WHERE seconds_read > 60 OR units_completed > 0 ORDER BY study_date DESC")
    active_dates = [r[0] for r in cursor.fetchall()]

    streak = 0
    curr_date = datetime.date.today()
    # Check if active today or yesterday
    if active_dates:
        latest = datetime.date.fromisoformat(active_dates[0])
        if (curr_date - latest).days <= 1:
            check_date = latest
            for d_str in active_dates:
                d = datetime.date.fromisoformat(d_str)
                if (check_date - d).days <= 1:
                    streak += 1
                    check_date = d
                else:
                    break

    conn.close()

    return {
        "completed_units": completed_units,
        "in_progress_units": in_progress_units,
        "total_minutes": round(total_seconds / 60, 1),
        "today_minutes": round(today_seconds / 60, 1),
        "today_units": today_units,
        "study_streak_days": max(1, streak) if today_seconds > 0 or today_units > 0 else streak
    }


def save_note(course_code: str, unit_id: str, content: str):
    """Saves personal study notes for a unit."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO unit_notes (course_code, unit_id, note_content, updated_at)
    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(course_code, unit_id) DO UPDATE SET
        note_content = excluded.note_content,
        updated_at = CURRENT_TIMESTAMP
    """, (course_code, unit_id, content))
    conn.commit()
    conn.close()


def get_note(course_code: str, unit_id: str) -> str:
    """Retrieves personal study notes for a unit."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT note_content FROM unit_notes WHERE course_code = ? AND unit_id = ?",
                   (course_code, unit_id))
    row = cursor.fetchone()
    conn.close()
    return row['note_content'] if row and row['note_content'] else ""


# Initialize on import
init_db()
