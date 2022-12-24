from aiogram.dispatcher.filters.state import StatesGroup, State


class PhotoInscription(StatesGroup):
    user_incription_config = State()
