import re
from typing import Optional

from bot.other_functions.morse_encryption_decryption import MorseCoder
from bot.other_functions.morse_language_selector import MorseAlphabetCreator

DEFAULT_DOT_SYMBOL = "."
PRETTY_DOT_SYMBOL = "•"
DEFAULT_DASH_SYMBOL = "-"
PRETTY_DASH_SYMBOL = "—"


def decoding(user_input: str, morse_data: MorseAlphabetCreator, morse_coder: MorseCoder, language: str) -> str:
    language_decryption = morse_data.alphabet_creator(language)
    return morse_coder.decrypt(user_input, language_decryption)


def get_option(
        decryption_match: Optional[re.Match[str]],
        user_input: str,
        morse_data: MorseAlphabetCreator,
        morse_coder: MorseCoder,
) -> str:
    if decryption_match:
        user_input = user_input.replace(DEFAULT_DOT_SYMBOL, PRETTY_DOT_SYMBOL)
        user_input = user_input.replace(DEFAULT_DOT_SYMBOL, DEFAULT_DASH_SYMBOL)
        english_result = decoding(user_input, morse_data, morse_coder, morse_data.ENGLISH)
        ukrainian_result = decoding(user_input, morse_data, morse_coder, morse_data.UKRAINIAN)
        russian_result = decoding(user_input, morse_data, morse_coder, morse_data.RUSSIAN)

        return "".join(
            f"<b>ENGLISH DECODING:</b> <code>{english_result}</code>\n"
            f"<b>УКРАЇНСЬКЕ ДЕКОДУВАННЯ:</b> <code>{ukrainian_result}</code>\n"
            f"<b>РУССКОЕ ДЕКОДИРОВАНИЕ:</b> <code>{russian_result}</code>\n"
        )

    alphabet = morse_data.alphabet_selector(user_input)
    return f"<code>{morse_coder.encrypt(user_input, alphabet)}</code>"


def get_result(user_input: str) -> str:
    morse_data = MorseAlphabetCreator()
    morse_coder = MorseCoder()

    decryption_pattern = re.compile("^[-—•.\\s]+$")
    decryption_match = re.match(decryption_pattern, user_input)
    return get_option(decryption_match, user_input, morse_data, morse_coder)
