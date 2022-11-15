from aiogram import types

from bot.bot_main import main_objects_initialization
from bot.bot_main.for_mem_creation.extract_random_data import get_random_data
from bot.bot_main.main_objects_initialization import dp, bot


@dp.message_handler(commands=['sticker'])
async def choose_sticker(message: types.Message):
    data = main_objects_initialization.extract_random_data.get_sticker()
    await bot.send_sticker(message.chat.id, sticker=f'{get_random_data(data)}')
    await message.delete()
