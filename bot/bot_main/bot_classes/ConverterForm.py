from aiogram.dispatcher.filters.state import StatesGroup, State


class ConverterForm(StatesGroup):
    dollar = State()
    euro = State()
    hryvnia = State()
