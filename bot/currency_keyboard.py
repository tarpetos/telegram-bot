from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

currency_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

exchange_rate_button = KeyboardButton(text='Курс валют')
converter_button = KeyboardButton(text='Конвертація')
close_button = KeyboardButton(text='Закрити клавіатуру')

currency_keyboard.add(exchange_rate_button).insert(converter_button).add(close_button)
