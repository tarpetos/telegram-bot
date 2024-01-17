from aiogram import types

from bot.config import dp
from bot.keyboards.password_generator.radio_keyboard import (
    first_generator_keyboard,
    all_button,
    letters_button,
    digits_button,
    let_dig_button,
    let_sig_button,
    dig_sig_button,
)
from bot.commands.commands_utils.change_state_mem_storage import update_state


def default_content_keyboard():
    all_button.text = "All characters"
    letters_button.text = "Only letters"
    digits_button.text = "Only digits"
    let_dig_button.text = "Letters & digits"
    let_sig_button.text = "Letters & signs"
    dig_sig_button.text = "Digits & signs"


@dp.callback_query_handler(text=["all_characters"])
async def option_all_characters(call: types.CallbackQuery):
    result = await update_state(call)

    await call.answer("Now your password can contain all possible characters!", True)

    if all_button.text == "All characters ✅":
        pass
    else:
        all_button.text = "All characters ✅"
        letters_button.text = "Only letters"
        digits_button.text = "Only digits"
        let_dig_button.text = "Letters & digits"
        let_sig_button.text = "Letters & signs"
        dig_sig_button.text = "Digits & signs"

        await call.message.edit_reply_markup(first_generator_keyboard)


@dp.callback_query_handler(text=["only_letters"])
async def option_only_letters(call: types.CallbackQuery):
    result = await update_state(call)
    await call.answer(
        "Now your password can contain only small and big english letters!", True
    )

    if letters_button.text == "Only letters ✅":
        pass
    else:
        all_button.text = "All characters"
        letters_button.text = "Only letters ✅"
        digits_button.text = "Only digits"
        let_dig_button.text = "Letters & digits"
        let_sig_button.text = "Letters & signs"
        dig_sig_button.text = "Digits & signs"

        await call.message.edit_reply_markup(first_generator_keyboard)


@dp.callback_query_handler(text=["only_digits"])
async def option_only_digits(call: types.CallbackQuery):
    result = await update_state(call)
    await call.answer("Now your password can contain only digits!", True)

    if digits_button.text == "Only digits ✅":
        pass
    else:
        all_button.text = "All characters"
        letters_button.text = "Only letters"
        digits_button.text = "Only digits ✅"
        let_dig_button.text = "Letters & digits"
        let_sig_button.text = "Letters & signs"
        dig_sig_button.text = "Digits & signs"

        await call.message.edit_reply_markup(first_generator_keyboard)


@dp.callback_query_handler(text=["letters_digits"])
async def option_letters_digits(call: types.CallbackQuery):
    result = await update_state(call)
    await call.answer("Now your password can contain english letters and digits!", True)

    if let_dig_button.text == "Letters & digits ✅":
        pass
    else:
        all_button.text = "All characters"
        letters_button.text = "Only letters"
        digits_button.text = "Only digits"
        let_dig_button.text = "Letters & digits ✅"
        let_sig_button.text = "Letters & signs"
        dig_sig_button.text = "Digits & signs"

        await call.message.edit_reply_markup(first_generator_keyboard)


@dp.callback_query_handler(text=["letters_signs"])
async def option_letters_signs(call: types.CallbackQuery):
    result = await update_state(call)
    await call.answer("Now your password can contain all letters and signs!", True)

    if let_sig_button.text == "Letters & signs ✅":
        pass
    else:
        all_button.text = "All characters"
        letters_button.text = "Only letters"
        digits_button.text = "Only digits"
        let_dig_button.text = "Letters & digits"
        let_sig_button.text = "Letters & signs ✅"
        dig_sig_button.text = "Digits & signs"

        await call.message.edit_reply_markup(first_generator_keyboard)


@dp.callback_query_handler(text=["digits_signs"])
async def option_digits_signs(call: types.CallbackQuery):
    result = await update_state(call)

    await call.answer("Now your password can contain digits and signs!", True)

    if dig_sig_button.text == "Digits & signs ✅":
        pass
    else:
        all_button.text = "All characters"
        letters_button.text = "Only letters"
        digits_button.text = "Only digits"
        let_dig_button.text = "Letters & digits"
        let_sig_button.text = "Letters & signs"
        dig_sig_button.text = "Digits & signs ✅"

        await call.message.edit_reply_markup(first_generator_keyboard)
