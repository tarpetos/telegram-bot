from random import choices


def main_generation(password_alphabet, password_length) -> str:
    return ''.join(choices(password_alphabet, k=password_length))
