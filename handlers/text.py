from aiogram import Router, types, F

from utils.logger import log_message

router = Router()

@router.message(F.text)
async def echo_handler(message: types.Message) -> None:
    """Echo incoming text messages."""
    username = message.from_user.username or message.from_user.full_name
    log_message(username, message.text)
    await message.answer(f"I am Hranitel. You said: {message.text}")
