from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

password_start_keyboard = InlineKeyboardMarkup()

telegram_app_button = InlineKeyboardButton(text='Move to telegram generator', callback_data='telegram_password')
app_button = InlineKeyboardButton(text='Download desktop application', callback_data='password_app')
close_button = InlineKeyboardButton(text='Close this menu', callback_data='close_app')

password_start_keyboard.add(telegram_app_button).insert(app_button).add(close_button)
