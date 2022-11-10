from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

random_number_keyboard = InlineKeyboardMarkup()

random_button1 = InlineKeyboardButton(text='Діапазон 0 — 10', callback_data='random_value_1')
random_button2 = InlineKeyboardButton(text='Діапазон 0 — 100', callback_data='random_value_2')
random_button3 = InlineKeyboardButton(text='Діапазон -100 — 100', callback_data='random_value_3')
random_button4 = InlineKeyboardButton(text='Діапазон -1000000 — 1000000', callback_data='random_value_4')

random_number_keyboard.add(random_button1).insert(random_button2).add(random_button3).insert(random_button4)
