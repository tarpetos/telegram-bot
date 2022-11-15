from aiogram import types

from bot.bot_main.main_objects_initialization import dp
from bot.bot_main.config import COMMANDS_LIST


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('ШТУЧНИЙ ІНТЕЛЕКТ ДТР-1')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=COMMANDS_LIST)
