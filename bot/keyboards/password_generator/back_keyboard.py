from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_to_telegram_generator_keyboard = InlineKeyboardMarkup()

back_button = InlineKeyboardButton(
    text="Back", callback_data="back_to_telegram_generator"
)

back_to_telegram_generator_keyboard.add(back_button)
