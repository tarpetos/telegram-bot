from random import choices
from string import punctuation


def exclude_invalid_symbols_for_markup() -> str:
    excluded_symbols = '<>&"'
    allowed_symbols = "".join(
        [char for char in punctuation if char not in excluded_symbols]
    )

    return allowed_symbols


def main_generation(password_alphabet: str, password_length: int) -> str:
    return "".join(choices(password_alphabet, k=password_length))
