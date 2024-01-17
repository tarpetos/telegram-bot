from typing import Dict

from .morse_alphabet import MORSE_CODE_DICT


class MorseAlphabetCreator:
    ENGLISH: str = "EN"
    CYRILLIC_DEFAULT: str = "CYRILLIC"
    UKRAINIAN: str = "UA"
    RUSSIAN: str = "RU"
    OTHER: str = "OTHER"

    def __init__(self):
        self.language = None

    def alphabet_selector(self, user_input: str) -> Dict[str, str]:
        data = user_input.upper()
        data_list = [char for char in data]

        english_alphabet = self.alphabet_creator(self.ENGLISH)
        ukrainian_alphabet = self.alphabet_creator(self.UKRAINIAN)
        russian_alphabet = self.alphabet_creator(self.RUSSIAN)

        if all(char in ukrainian_alphabet for char in data_list):
            return ukrainian_alphabet
        elif all(char in russian_alphabet for char in data_list):
            return russian_alphabet
        return english_alphabet

    def alphabet_creator(self, language_choice: str) -> Dict[str, str]:
        result_dict = {}

        if language_choice == self.ENGLISH:
            result_dict.update(MORSE_CODE_DICT[language_choice])
        else:
            result_dict.update(MORSE_CODE_DICT[self.CYRILLIC_DEFAULT])
            result_dict.update(MORSE_CODE_DICT[language_choice])

        result_dict.update(MORSE_CODE_DICT[self.OTHER])
        return result_dict
