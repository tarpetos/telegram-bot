from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

return_keyboard = InlineKeyboardMarkup()

return_button = InlineKeyboardButton(text='Return to main menu', callback_data='back_to_menu')

return_keyboard.add(return_button)
