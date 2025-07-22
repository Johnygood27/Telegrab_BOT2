"""Handler for the /start command."""
from __future__ import annotations

from aiogram import Router, types
from aiogram.filters import Command

from config import ASCII_LOGO
from utils.logger import log_to_db
from utils.rate_limiter import check_rate_limit

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message) -> None:
    """Send welcome message with ASCII logo."""
    if not check_rate_limit(message.from_user.id):
        return
    conn = message.bot.get("db")
    username = message.from_user.username or message.from_user.full_name
    await log_to_db(conn, username, message.from_user.id, message.text or "")
    text = f"<pre>{ASCII_LOGO}</pre>\nI am HRANITEL. I gather. I protect. I serve."
    await message.answer(text)
