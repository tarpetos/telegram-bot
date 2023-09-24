from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

random_number_keyboard = InlineKeyboardMarkup()

random_button1 = InlineKeyboardButton(
    text="Range 0 — 10", callback_data="random_value_1"
)
random_button2 = InlineKeyboardButton(
    text="Range 0 — 100", callback_data="random_value_2"
)
random_button3 = InlineKeyboardButton(
    text="Range -100 — 100", callback_data="random_value_3"
)
random_button4 = InlineKeyboardButton(
    text="Range -1000000 — 1000000", callback_data="random_value_4"
)
close_button = InlineKeyboardButton(text="Close keyboard", callback_data="close_random")

random_number_keyboard.add(random_button1)
random_number_keyboard.insert(random_button2)
random_number_keyboard.add(random_button3)
random_number_keyboard.insert(random_button4)
random_number_keyboard.add(close_button)
