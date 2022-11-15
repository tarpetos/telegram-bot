from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.bot_main.bot_classes.CreateUniqueTables import CreateUniqueTables
from bot.bot_main.bot_classes.ExtractRandomData import ExtractRandomData
from bot.bot_main.bot_classes.RandomDataTables import RandomDataTables
from bot.bot_main.bot_classes.StoreUsersData import StoreUsersData
from bot.bot_main.config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

create_tables = RandomDataTables()
extract_random_data = ExtractRandomData(create_tables)
store_users_data = StoreUsersData()
table = CreateUniqueTables()
