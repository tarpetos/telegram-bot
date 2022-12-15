API_TOKEN = '5063348094:AAFQCdPM_0UdIo9lmisS-1FIoJAaSpuZO-w'

UA_COMMAND_DESC_LIST = '''
/start - перевірка роботи бота
/random - генерація випадкового цілого числа
/eugene - функція пошуку відео
/id - інформація про користувача
/time - дата, поточний час та інша інформація стосовно часу
/sticker - відправляє випадковий стікер
/currency - конвертер валют
/weather - погода в заданому населеному пункті
/birthday - обрахунок днів до заданої дати
/taskscheduler - планувальник завдань
/photo - додавання тексту на фото, зміна розмірів фото
/password - генератор випадкових паролів
/keywords - список ключових слів, на які реагує бот
/help - список команд
'''

EN_COMMAND_DESC_LIST = '''
/start - check if bot is working
/random - generate random integer number
/eugene - youtube video search
/id - information about user
/time - current date, time and other time info
/sticker - send a random sticker
/currency - currency converter
/weather - show the weather in the entered settlement
/birthday - calculate number of days from current date to another
/taskscheduler - create a list of tasks
/photo - adding text to photo, change photo size
/password - random password generator
/keywords - list of keywords that the bot responds to
/help - command list
'''

COMMAND_LIST = [
    '/start',
    '/random',
    '/eugene',
    '/id',
    '/time',
    '/sticker',
    '/currency',
    '/weather',
    '/birthday',
    '/taskscheduler',
    '/photo',
    '/password',
    '/keywords',
    '/help',
]

CURRENCY_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
BITCOIN_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
