from random import choices
from string import digits, ascii_letters, punctuation


def exclude_invalid_symbols_for_markup() -> str:
    excluded_symbols = '<>&"'
    allowed_symbols = "".join(
        [char for char in punctuation if char not in excluded_symbols]
    )

    return allowed_symbols


def main_generation(password_alphabet: str, password_length: int) -> str:
    return "".join(choices(password_alphabet, k=password_length))


def generate_token() -> str:
    token_alphabet = ascii_letters + digits + exclude_invalid_symbols_for_markup()

    return "".join(choices(token_alphabet, k=50))
