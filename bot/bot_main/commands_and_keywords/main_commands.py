from aiogram import types

from bot.bot_main.main_objects_initialization import dp
from config import EN_COMMAND_DESC_LIST


@dp.message_handler(state='*', commands=['start'])
async def start_command(message: types.Message):
    await message.reply('I am activated. Type your commands or keywords.')


@dp.message_handler(state='*', commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=EN_COMMAND_DESC_LIST)
