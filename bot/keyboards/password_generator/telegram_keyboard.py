from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.password_generator.return_keyboard import return_button

password_telegram_keyboard = InlineKeyboardMarkup()

show_passwords_button = InlineKeyboardButton(text='Show all passwords', callback_data='show_password')
create_password_button = InlineKeyboardButton(text='Generate password', callback_data='create_password')
change_password_button = InlineKeyboardButton(text='Change password', callback_data='change_desc_pass')
delete_password_button = InlineKeyboardButton(text='Delete password', callback_data='delete_password')
get_json_button = InlineKeyboardButton(text='Get all passwords in json', callback_data='json_password')

password_telegram_keyboard.add(show_passwords_button)
password_telegram_keyboard.insert(create_password_button)
password_telegram_keyboard.add(change_password_button)
password_telegram_keyboard.insert(delete_password_button)
password_telegram_keyboard.add(get_json_button)
password_telegram_keyboard.add(return_button)
