from typing import Dict, List


class MorseCoder:
    EMPTY_SPACE: str = " "
    EMPTY_STRING: str = ""
    UNKNOWN_SYMBOL: str = "�"

    def encrypt(self, text_data: str, morse_alphabet: Dict[str, str]) -> str:
        text_data: str = text_data.upper()

        encrypted_message = [
            self.EMPTY_SPACE
            if char == self.EMPTY_SPACE
            else (morse_alphabet.get(char, self.UNKNOWN_SYMBOL) + self.EMPTY_SPACE)
            for char in text_data
        ]
        return "".join(encrypted_message).strip()

    def decrypt(self, encrypted_data: str, morse_alphabet: Dict[str, str]) -> str:
        encrypted_data_list: List[str] = encrypted_data.split(self.EMPTY_SPACE)

        decrypted_message = [
            self.EMPTY_SPACE
            if enc_char == self.EMPTY_STRING
            else next(
                (key for key, val in morse_alphabet.items() if val == enc_char),
                self.UNKNOWN_SYMBOL.strip(),
            )
            for enc_char in encrypted_data_list
        ]
        return "".join(decrypted_message)
