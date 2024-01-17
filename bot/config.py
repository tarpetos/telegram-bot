import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv

from .db_utils.unique_tables_creator import UniqueTablesCreator

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("API_TOKEN")

COMMANDS_DESCRIPTION = """
/start - <b>check if bot is working</b>
/time - <b>current date, time and other time info</b>
/date_calculator - <b>calculate number of days from one date to another</b>
/current_weather - <b>show the weather in the entered settlement</b>
/image_editor - <b>adding text to photo, change photo size</b>
/currency_converter - <b>currency converter</b>
/password_generator - <b>random password generator</b>
/task_scheduler - <b>create a list of tasks</b>
/keyword_list - <b>list of keywords that the bot responds to</b>
/help - <b>command list</b>
"""

CURRENCY_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=11"
BITCOIN_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

# PROXY_URL = "http://proxy.server:3128"
# bot = Bot(token=BOT_TOKEN, proxy=PROXY_URL)
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
unique_table = UniqueTablesCreator()
