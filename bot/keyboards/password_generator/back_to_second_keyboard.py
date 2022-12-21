from aiogram.types import InlineKeyboardMarkup

from bot.keyboards.password_generator.generation_keyboard import back_button

password_generator_back_to_second = InlineKeyboardMarkup()

password_generator_back_to_second.add(back_button)
