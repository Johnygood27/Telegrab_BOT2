"""Handler for the /help command."""
from __future__ import annotations

from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_handler(message: types.Message) -> None:
    """Provide help information."""
    text = (
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message"
    )
    await message.answer(text)
