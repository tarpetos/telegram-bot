from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherInfo(StatesGroup):
    place = State()
