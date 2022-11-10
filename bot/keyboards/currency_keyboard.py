from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

currency_keyboard = InlineKeyboardMarkup()

exchange_rate_button = InlineKeyboardButton(text='Курс валют', callback_data='currency_rate')
converter_button = InlineKeyboardButton(text='Конвертація', callback_data='currency_converter')

currency_keyboard.add(exchange_rate_button).insert(converter_button)
