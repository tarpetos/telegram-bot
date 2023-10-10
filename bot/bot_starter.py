from aiogram.utils import executor
from .config import dp


class MyBot:
    def start(self) -> None:
        return executor.start_polling(dp, skip_updates=True)
