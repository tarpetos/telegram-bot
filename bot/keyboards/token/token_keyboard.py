from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

token_keyboard = InlineKeyboardMarkup()

new_token_button = InlineKeyboardButton(
    text="Generate new token", callback_data="add_token"
)
delete_token_button = InlineKeyboardButton(
    text="Remove token", callback_data="delete_token"
)
close_keyboard_button = InlineKeyboardButton(
    text="Close keyboard", callback_data="close_token"
)

token_keyboard.add(new_token_button).insert(delete_token_button).add(
    close_keyboard_button
)