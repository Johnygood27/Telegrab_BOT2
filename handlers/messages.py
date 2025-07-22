"""Handler for incoming text messages."""
from __future__ import annotations

from aiogram import Router, types, F

from utils.logger import log_to_db
from utils.rate_limiter import check_rate_limit

router = Router()


@router.message(F.text)
async def text_handler(message: types.Message) -> None:
    """Log and acknowledge text messages."""
    if not check_rate_limit(message.from_user.id):
        return
    conn = message.bot.get("db")
    username = message.from_user.username or message.from_user.full_name
    await log_to_db(conn, username, message.from_user.id, message.text or "")
    await message.answer("Your message has been logged. Analyzing...")
