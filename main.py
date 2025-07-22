"""Entry point for HRANITEL bot."""
from __future__ import annotations

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings, ASCII_LOGO
from handlers import help_router, messages_router, start_router
from storage.db import init_db
from utils.logger import setup_logging


async def main() -> None:
    """Start the bot."""
    setup_logging()
    print(ASCII_LOGO)
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(messages_router)

    db_conn = await init_db(settings.db_path)
    bot["db"] = db_conn

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
