from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.password_generator.back_keyboard import back_button

first_generator_keyboard = InlineKeyboardMarkup()

all_button = InlineKeyboardButton(text="All characters", callback_data="all_characters")
letters_button = InlineKeyboardButton(text="Only letters", callback_data="only_letters")
digits_button = InlineKeyboardButton(text="Only digits", callback_data="only_digits")
let_dig_button = InlineKeyboardButton(
    text="Letters & digits", callback_data="letters_digits"
)
let_sig_button = InlineKeyboardButton(
    text="Letters & signs", callback_data="letters_signs"
)
dig_sig_button = InlineKeyboardButton(
    text="Digits & signs", callback_data="digits_signs"
)
next_button = InlineKeyboardButton(text="Next", callback_data="next_to_second")

first_generator_keyboard.add(all_button)
first_generator_keyboard.add(letters_button)
first_generator_keyboard.add(digits_button)
first_generator_keyboard.add(let_dig_button)
first_generator_keyboard.add(let_sig_button)
first_generator_keyboard.add(dig_sig_button)
first_generator_keyboard.add(back_button)
first_generator_keyboard.insert(next_button)
