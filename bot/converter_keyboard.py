from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from currency_keyboard import close_button

converter_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

dollar_button = KeyboardButton(text='Конвертація долара')
euro_button = KeyboardButton(text='Конвертація євро')
hryvnia_button = KeyboardButton(text='Конвертація гривні')
return_button = KeyboardButton(text='До головного меню')

converter_keyboard.add(dollar_button).add(euro_button).add(hryvnia_button).add(return_button).insert(close_button)
