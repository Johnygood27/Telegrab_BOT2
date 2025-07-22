"""Simple per-user rate limiter."""
from __future__ import annotations

from time import time
from typing import Dict

RATE_LIMIT_SECONDS = 5
_last_time: Dict[int, float] = {}


def check_rate_limit(user_id: int) -> bool:
    """Return True if the user is allowed to send a message."""
    now = time()
    last = _last_time.get(user_id, 0)
    if now - last < RATE_LIMIT_SECONDS:
        return False
    _last_time[user_id] = now
    return True
