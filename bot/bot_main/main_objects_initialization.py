from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.bot_main.bot_classes.StatisticsTable import StatisticsTable
from bot.bot_main.bot_classes.UniqueTablesForUsers import UniqueTablesForUsers
from bot.bot_main.bot_classes.UserToken import UserToken
from bot.bot_main.bot_classes.UsersDataStore import UsersDataStore
from bot.bot_main.bot_classes.StickerTable import StickerTable
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

store_users_data = UsersDataStore()
statistics_table = StatisticsTable()
unique_table = UniqueTablesForUsers()
sticker_table = StickerTable()
token_table = UserToken()
