from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

converter_keyboard = InlineKeyboardMarkup()

dollar_button = InlineKeyboardButton(text='Конвертація долара', callback_data='convert_dollar')
euro_button = InlineKeyboardButton(text='Конвертація євро', callback_data='convert_euro')
hryvnia_button = InlineKeyboardButton(text='Конвертація гривні', callback_data='convert_hryvnia')
return_button = InlineKeyboardButton(text='До головного меню', callback_data='back_to_menu')

converter_keyboard.add(dollar_button).add(euro_button).add(hryvnia_button).add(return_button)
