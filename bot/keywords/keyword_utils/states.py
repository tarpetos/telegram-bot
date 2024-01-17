from aiogram.dispatcher.filters.state import StatesGroup, State


class ImageSaver(StatesGroup):
    image = State()
