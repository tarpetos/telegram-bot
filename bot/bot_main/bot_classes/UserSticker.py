from aiogram.dispatcher.filters.state import StatesGroup, State


class UserSticker(StatesGroup):
    user_sticker = State()
