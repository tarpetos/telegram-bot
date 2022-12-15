from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

return_app_keyboard = InlineKeyboardMarkup()

return_button = InlineKeyboardButton(text='Return to main menu', callback_data='back_to_main_menu')

return_app_keyboard.add(return_button)