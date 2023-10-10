from string import digits, ascii_letters

from bot.bot_main.for_password_generation.generate_password import (
    exclude_invalid_symbols_for_markup,
)


def keyboard_content_choice(user_choice) -> str:
    allowed_punctuation = exclude_invalid_symbols_for_markup()
    if user_choice == "all_characters":
        return digits + ascii_letters + allowed_punctuation
    elif user_choice == "only_letters":
        return ascii_letters
    elif user_choice == "only_digits":
        return digits
    elif user_choice == "letters_digits":
        return digits + ascii_letters
    elif user_choice == "letters_signs":
        return ascii_letters + allowed_punctuation
    elif user_choice == "digits_signs":
        return digits + allowed_punctuation
