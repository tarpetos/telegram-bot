from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

password_generator_return_to_update = InlineKeyboardMarkup()

return_button = InlineKeyboardButton(text="Back", callback_data="return_to_update_menu")

password_generator_return_to_update.add(return_button)
