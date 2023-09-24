from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

second_generator_keyboard = InlineKeyboardMarkup()

very_easy_button = InlineKeyboardButton(text="Very easy", callback_data="very_easy")
easy_button = InlineKeyboardButton(text="Easy", callback_data="easy")
normal_button = InlineKeyboardButton(text="Normal", callback_data="normal")
hard_button = InlineKeyboardButton(text="Hard", callback_data="hard")
very_hard_button = InlineKeyboardButton(text="Very hard", callback_data="very_hard")
unbreakable_button = InlineKeyboardButton(
    text="Unbreakable", callback_data="unbreakable"
)

back_button = InlineKeyboardButton(text="Back", callback_data="back_to_first")
next_button = InlineKeyboardButton(text="Next", callback_data="next_to_third")


second_generator_keyboard.add(very_easy_button)
second_generator_keyboard.add(easy_button)
second_generator_keyboard.add(normal_button)
second_generator_keyboard.add(hard_button)
second_generator_keyboard.add(very_hard_button)
second_generator_keyboard.add(unbreakable_button)
second_generator_keyboard.add(back_button)
second_generator_keyboard.insert(next_button)
