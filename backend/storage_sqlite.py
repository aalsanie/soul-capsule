import sqlite3
import json
from backend.models import CapsuleResponse

DB_PATH = "capsules.db"  # Default DB path


def set_db_path(path: str):
    global DB_PATH
    DB_PATH = path


def save_capsule_sqlite(capsule: CapsuleResponse):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO capsules (id, raw_input, generated_summary, style, emotion_vector, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        capsule.id,
        capsule.raw_input,
        capsule.generated_summary,
        capsule.style,
        json.dumps(capsule.emotion_vector),
        capsule.timestamp.isoformat() if capsule.timestamp else None
    ))
    conn.commit()
    conn.close()


def load_capsule_sqlite(capsule_id: str) -> CapsuleResponse | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM capsules WHERE id = ?", (capsule_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return CapsuleResponse(
            id=row[0],
            raw_input=row[1],
            generated_summary=row[2],
            style=row[3],
            emotion_vector=json.loads(row[4]),
            timestamp=row[5]
        )
    return None


def list_capsules_sqlite(style=None, emotion=None, limit=None) -> list[CapsuleResponse]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT * FROM capsules"
    filters = []
    params = []

    if style:
        filters.append("style = ?")
        params.append(style)
    if emotion:
        filters.append("emotion_vector LIKE ?")
        params.append(f'%{emotion}%')

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY timestamp DESC"

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    capsules = []
    for row in rows:
        capsules.append(CapsuleResponse(
            id=row[0],
            raw_input=row[1],
            generated_summary=row[2],
            style=row[3],
            emotion_vector=json.loads(row[4]),
            timestamp=row[5]
        ))
    return capsules

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS capsules (
            id TEXT PRIMARY KEY,
            raw_input TEXT,
            generated_summary TEXT,
            style TEXT,
            emotion_vector TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()
