from aiogram import types

from ..config import dp
from ..enums import Command


@dp.message_handler(state="*", commands=Command.START)
async def start_command_handler(message: types.Message):
    await message.reply(
        f"<code>{message.from_user.full_name}</code>, I am activated. "
        f"Type commands or keywords. Use /help command to see the list of possible actions.",
        parse_mode="HTML"
    )
