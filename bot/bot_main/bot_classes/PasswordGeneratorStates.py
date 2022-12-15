from aiogram.dispatcher.filters.state import StatesGroup, State


class PasswordGeneratorStates(StatesGroup):
    update_description = State()
    update_password = State()
    delete = State()

    set_description = State()
    set_length = State()

    # radio_all_characters = State()
    # radio_only_letters = State()
    # radio_only_digits = State()
    # radio_letters_digits = State()
    # radio_letters_signs = State()
    # radio_digits_signs = State()
