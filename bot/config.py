import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv

from .bot_main.bot_classes.UniqueTablesForUsers import UniqueTablesForUsers

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("API_TOKEN")

EN_COMMAND_DESC_LIST = """
/start - check if bot is working
/random - generate random integer number
/eugene - youtube video search
/time - current date, time and other time info
/currency - currency converter
/weather - show the weather in the entered settlement
/birthday - calculate number of days from current date to another
/taskscheduler - create a list of tasks
/photo - adding text to photo, change photo size
/password - random password generator
/keywords - list of keywords that the bot responds to
/help - command list
"""

# CURRENCY_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
CURRENCY_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=11"
# BITCOIN_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
BITCOIN_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

# PROXY_URL = "http://proxy.server:3128"
# bot = Bot(token=BOT_TOKEN, proxy=PROXY_URL)
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
unique_table = UniqueTablesForUsers()
