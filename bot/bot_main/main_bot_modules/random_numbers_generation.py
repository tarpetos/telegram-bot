from random import randint

from aiogram import types

from bot.bot_main.main_objects_initialization import dp
from bot.keyboards import random_numbers_keyboard


@dp.message_handler(commands=['random'])
async def randomize(message: types.Message):
    await message.reply('Виберіть діапазон числа:', reply_markup=random_numbers_keyboard.random_number_keyboard)


@dp.callback_query_handler(text=['random_value_1', 'random_value_2', 'random_value_3', 'random_value_4'])
async def choose_random(call: types.CallbackQuery):
    if call.data == 'random_value_1':
        await call.answer(f'Згенероване випадкове число: {randint(0, 10)} 🎲')
    elif call.data == 'random_value_2':
        await call.answer(f'Згенероване випадкове число: {randint(0, 100)} 🎲')
    elif call.data == 'random_value_3':
        await call.answer(f'Згенероване випадкове число: {randint(-100, 100)} 🎲')
    elif call.data == 'random_value_4':
        await call.answer(f'Згенероване випадкове число: {randint(-1000000, 1000000)} 🎲')

    await call.answer()
