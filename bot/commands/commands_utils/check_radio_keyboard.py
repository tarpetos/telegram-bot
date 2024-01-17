from string import digits, ascii_letters

from bot.commands.commands_utils.generate_password import (
    exclude_invalid_symbols_for_markup,
)


def keyboard_content_choice(user_choice: str) -> str:
    allowed_punctuation = exclude_invalid_symbols_for_markup()

    password_content_options = {
        "all_characters": digits + ascii_letters + allowed_punctuation,
        "only_letters": ascii_letters,
        "only_digits": digits,
        "letters_digits": digits + ascii_letters,
        "letters_signs": ascii_letters + allowed_punctuation,
        "digits_signs": digits + allowed_punctuation,
    }

    for content_option_key in password_content_options:
        if user_choice == content_option_key:
            return password_content_options[content_option_key]
