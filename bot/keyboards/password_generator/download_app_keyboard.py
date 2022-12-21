from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.password_generator.return_keyboard import return_button

download_app_keyboard = InlineKeyboardMarkup()

windows_button = InlineKeyboardButton(text='Windows installer', callback_data='windows_installer')
linux_mac_button = InlineKeyboardButton(text='Linux/MacOS binary', callback_data='linux_macos')

download_app_keyboard.add(windows_button).insert(linux_mac_button).add(return_button)
