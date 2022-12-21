from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.currency_converter.return_keyboard import return_button

converter_keyboard = InlineKeyboardMarkup()

dollar_button = InlineKeyboardButton(text='Dollar conversion', callback_data='convert_dollar')
euro_button = InlineKeyboardButton(text='Euro conversion', callback_data='convert_euro')
hryvnia_button = InlineKeyboardButton(text='Hryvnia conversion', callback_data='convert_hryvnia')

converter_keyboard.add(dollar_button).add(euro_button).add(hryvnia_button).add(return_button)
