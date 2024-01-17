from aiogram import types

from ..config import dp
from ..config import COMMANDS_DESCRIPTION
from ..enums import Command


@dp.message_handler(state="*", commands=Command.HELP)
async def help_command_handler(message: types.Message):
    await message.reply(text=COMMANDS_DESCRIPTION, parse_mode="HTML")
