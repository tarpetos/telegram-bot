from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

currency_keyboard = InlineKeyboardMarkup()

exchange_rate_button = InlineKeyboardButton(text='Exchange rate', callback_data='currency_rate')
converter_button = InlineKeyboardButton(text='Converter', callback_data='currency_converter')
close_button = InlineKeyboardButton(text='Close keyboard', callback_data='close_converter')

currency_keyboard.add(exchange_rate_button).insert(converter_button).add(close_button)
