from random import randint

from aiogram import types

from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.random_number import random_numbers_keyboard
from bot.other_functions.close_keyboard import close_keyboard


@dp.message_handler(state="*", commands=["random"])
async def randomize(message: types.Message):
    await message.reply(
        "Select a number range: ",
        reply_markup=random_numbers_keyboard.random_number_keyboard,
    )


@dp.callback_query_handler(
    text=["random_value_1", "random_value_2", "random_value_3", "random_value_4"]
)
async def choose_random(call: types.CallbackQuery):
    if call.data == "random_value_1":
        await call.answer(f"Generated random number: {randint(0, 10)} 🎲", True)
    elif call.data == "random_value_2":
        await call.answer(f"Generated random number: {randint(0, 100)} 🎲", True)
    elif call.data == "random_value_3":
        await call.answer(f"Generated random number: {randint(-100, 100)} 🎲", True)
    elif call.data == "random_value_4":
        await call.answer(
            f"Generated random number: \n{randint(-1000000, 1000000)} 🎲", True
        )

    await call.answer()


@dp.callback_query_handler(text=["close_random"])
async def close_random(call: types.CallbackQuery):
    await close_keyboard(call)
