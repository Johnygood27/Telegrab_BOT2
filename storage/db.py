"""SQLite logging utilities for HRANITEL."""
from __future__ import annotations

import aiosqlite

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    user_id INTEGER,
    timestamp TEXT,
    content TEXT
)
"""

async def init_db(path: str) -> aiosqlite.Connection:
    """Initializes the SQLite database and returns a connection."""
    conn = await aiosqlite.connect(path)
    await conn.execute(CREATE_TABLE_QUERY)
    await conn.commit()
    return conn

async def log_message(conn: aiosqlite.Connection, username: str, user_id: int, timestamp: str, content: str) -> None:
    """Store a message in the database."""
    await conn.execute(
        "INSERT INTO messages (username, user_id, timestamp, content) VALUES (?, ?, ?, ?)",
        (username, user_id, timestamp, content),
    )
    await conn.commit()
