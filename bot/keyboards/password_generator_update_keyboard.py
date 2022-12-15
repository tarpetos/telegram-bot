from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.password_generator_back_keyboard import back_button

password_generator_update_keyboard = InlineKeyboardMarkup()

change_description_button = InlineKeyboardButton(text='Change description', callback_data='change_description')
create_password_button = InlineKeyboardButton(text='Change password', callback_data='change_password')

password_generator_update_keyboard.add(change_description_button)
password_generator_update_keyboard.insert(create_password_button)
password_generator_update_keyboard.add(back_button)
