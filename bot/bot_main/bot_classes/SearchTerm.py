from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchTerm(StatesGroup):
    search_term = State()
