from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

third_generator_keyboard = InlineKeyboardMarkup()

generate_button = InlineKeyboardButton(
    text="Generate password", callback_data="generate_password"
)
write_to_db_button = InlineKeyboardButton(
    text="Store in database", callback_data="store_in_db"
)
back_button = InlineKeyboardButton(text="Back", callback_data="back_to_second")
return_to_start = InlineKeyboardButton(
    text="Main generator menu", callback_data="main_generator_menu"
)

third_generator_keyboard.add(generate_button)
third_generator_keyboard.insert(write_to_db_button)
third_generator_keyboard.add(back_button)
third_generator_keyboard.insert(return_to_start)
