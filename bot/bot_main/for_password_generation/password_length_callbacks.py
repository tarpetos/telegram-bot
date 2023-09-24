from typing import Coroutine, Any, Dict

from aiogram import types
from aiogram.types import InlineKeyboardButton

from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.password_generator.set_length_keyboard import (
    very_easy_button,
    easy_button,
    normal_button,
    hard_button,
    very_hard_button,
    unbreakable_button,
    second_generator_keyboard,
)
from bot.other_functions.change_state_mem_storage import update_with_length_state


class LengthController:
    BUTTON_OPTIONS: Dict[InlineKeyboardButton, str] = {
        very_easy_button: "Very easy",
        easy_button: "Easy",
        normal_button: "Normal",
        hard_button: "Hard",
        very_hard_button: "Very hard",
        unbreakable_button: "Unbreakable",
    }
    OPTION_SELECTED_SYMBOL: str = " ✅"
    EMPTY_STRING: str = ""

    async def select_option(
        self,
        call: types.CallbackQuery,
        result: Coroutine[Any, Any, dict | None],
        button: InlineKeyboardButton,
    ) -> None:
        if result is not None and self.OPTION_SELECTED_SYMBOL not in button.text:
            for button_option in self.BUTTON_OPTIONS:
                normal_option = self.try_get_option(button_option)
                self.check_for_selection(button_option, button, normal_option)
            await call.message.edit_reply_markup(second_generator_keyboard)

    def check_for_selection(
        self,
        current_button: InlineKeyboardButton,
        selected_button: InlineKeyboardButton,
        option_data: str,
    ) -> None:
        if current_button != selected_button:
            current_button.text = option_data
        else:
            current_button.text = option_data + self.OPTION_SELECTED_SYMBOL

    def back_to_default_keyboard(self) -> None:
        for button_option in self.BUTTON_OPTIONS:
            button_option.text = self.try_get_option(button_option)

    def try_get_option(self, chosen_option: InlineKeyboardButton) -> str:
        try:
            return self.BUTTON_OPTIONS[chosen_option]
        except KeyError:
            return chosen_option.text.replace(
                self.OPTION_SELECTED_SYMBOL, self.EMPTY_STRING
            )


@dp.callback_query_handler(
    lambda call: call.data
    in ["very_easy", "easy", "normal", "hard", "very_hard", "unbreakable"]
)
async def handle_difficulty_option(call: types.CallbackQuery):
    button_mapping = {
        "very_easy": very_easy_button,
        "easy": easy_button,
        "normal": normal_button,
        "hard": hard_button,
        "very_hard": very_hard_button,
        "unbreakable": unbreakable_button,
    }

    option = call.data
    result = await update_with_length_state(call)
    length_controller = LengthController()
    button = button_mapping.get(option)
    await length_controller.select_option(call, result, button)
