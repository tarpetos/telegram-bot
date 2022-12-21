from aiogram.dispatcher.filters.state import StatesGroup, State


class PasswordGeneratorStates(StatesGroup):
    update_description = State()
    update_password = State()
    delete = State()

    set_description = State()
