from aiogram.dispatcher.filters.state import StatesGroup, State


class DaysToBirthday(StatesGroup):
    day_month = State()
