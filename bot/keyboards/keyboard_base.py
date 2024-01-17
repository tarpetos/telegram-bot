from typing import Any

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class KeyboardBuilder(InlineKeyboardMarkup):
    def _make_button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    def add_column_button(self, text: str, callback_data: str) -> Any:
        return self.add(self._make_button(text, callback_data))

    def add_row_button(self, text: str, callback_data: str) -> Any:
        return self.insert(self._make_button(text, callback_data))
