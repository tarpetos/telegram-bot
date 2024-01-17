from aiogram.dispatcher.filters.state import StatesGroup, State


class ConverterForm(StatesGroup):
    dollar = State()
    euro = State()
    hryvnia = State()


class DaysToBirthday(StatesGroup):
    day_month = State()


class PasswordGeneratorStates(StatesGroup):
    update_description = State()
    update_password = State()
    delete = State()
    set_description = State()


class PhotoInscription(StatesGroup):
    user_inscription_config = State()


class SearchTerm(StatesGroup):
    search_term = State()


class TaskScheduler(StatesGroup):
    insert = State()
    update = State()
    delete = State()


class WeatherInfo(StatesGroup):
    place = State()
