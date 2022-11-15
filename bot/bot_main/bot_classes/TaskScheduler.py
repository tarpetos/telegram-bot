from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskScheduler(StatesGroup):
    insert = State()
    update = State()
    delete = State()
