import asyncio

from aiogram import types

from bot.bot_main.main_objects_initialization import dp, bot
from config import EN_COMMAND_DESC_LIST


# DELETE_TIMEOUT = 60


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_message = message.message_id
    bot_message = await message.reply('I am activated. Type your commands or keywords.')

    # await asyncio.sleep(DELETE_TIMEOUT)
    # await bot.delete_message(chat_id=message.chat.id, message_id=user_message)
    # await bot.delete_message(chat_id=message.chat.id, message_id=bot_message.message_id)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_message = message.message_id
    bot_message = await message.reply(text=EN_COMMAND_DESC_LIST)

    # await asyncio.sleep(DELETE_TIMEOUT)
    # await bot.delete_message(chat_id=message.chat.id, message_id=user_message)
    # await bot.delete_message(chat_id=message.chat.id, message_id=bot_message.message_id)
