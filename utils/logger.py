"""Logging utilities for HRANITEL."""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from storage.db import log_message as db_log_message


LOG_FILE_NAME = "error.log"


def setup_logging() -> None:
    """Configure application-wide logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=LOG_FILE_NAME,
        filemode="a",
    )


async def log_to_db(conn: Any, username: str, user_id: int, text: str) -> None:
    """Log a message to the SQLite database."""
    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
    await db_log_message(conn, username, user_id, timestamp, text)
