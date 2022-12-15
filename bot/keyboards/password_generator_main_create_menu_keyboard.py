from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

second_generator_keyboard = InlineKeyboardMarkup()

description_button = InlineKeyboardButton(text='Enter description', callback_data='set_description')
length_button = InlineKeyboardButton(text='Enter length', callback_data='set_length')
back_button = InlineKeyboardButton(text='Back', callback_data='back_to_first')
next_button = InlineKeyboardButton(text='Next', callback_data='next_to_third')

second_generator_keyboard.add(description_button).add(length_button).add(back_button).insert(next_button)
# first_generator_keyboard.add(description_button).add(length_button).add(back_button)
