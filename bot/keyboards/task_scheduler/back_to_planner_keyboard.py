from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

return_keyboard = InlineKeyboardMarkup()

return_button = InlineKeyboardButton(text='Back', callback_data='back_to_scheduler')

return_keyboard.add(return_button)
