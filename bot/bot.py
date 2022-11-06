import random
import time
import extract_random_data
import create_meme

from aiogram.types import InputFile
from config import API_TOKEN
from datetime import date
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

COMMANDS_LIST = """
/start - перевірка роботи бота
/random - генерація випадкового цілого числа
/eugene - незавершена функція
/id - інформація про користувача
/time - дата, поточний час та інша інформація стосовно часу
/sticker - відправляє випадковий стікер
/currency - конвертер валют
/help - список команд
"""


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Я - БОС!!!😎')
    await message.delete()


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(text=COMMANDS_LIST)


@dp.message_handler(commands=['random'])
async def send_welcome(message: types.Message):
    random_number = random.randint(-1000000, 1000000)
    await message.reply(f'Згенероване випадкове число: {random_number}🎲')


@dp.message_handler(commands=['eugene'])
async def mark_eugene(message: types.Message):
    await message.reply('Команда "eugene" тимчасово не працює.🤷‍')


@dp.message_handler(commands=['id'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('ID', callback_data='user_id')
    keyboard_markup.row(user_id_btn)

    if message.from_user.username is not None:
        message.from_user.username = f'<code>{message.from_user.username}‍</code>'
    else:
        message.from_user.username = f'<span class="tg-spoiler"><b><i>користувач не має імені🤷</i></b></span>'

    await message.answer(f'Ім’я користувача: {message.from_user.username}\n'
                         f'URL: {message.from_user.url}\n\n'
                         'Натисни кнопку, щоб побачити свій ID...', parse_mode='HTML', reply_markup=keyboard_markup)


@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f"Ваш ID: {callback_query.from_user.id}", True)


@dp.message_handler(commands=['time'])
async def search_time(message: types.Message):
    delta = date(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday) - date(2022, 2, 23)
    days_of_unity = date(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday) - date(1919, 1,
                                                                                                             21)

    await message.reply(
        f'Поточна дата:\t{datetime.now().strftime("%d.%m.%Y")}📅\n'
        f'Поточний час:\t{datetime.now().strftime("%H:%M:%S")}🕔\n'
        f'День тижня:\t{datetime.now().strftime("%A")}\n'
        f'День року:\t{time.localtime().tm_yday}🌞\n'
        f'К-сть днів з початку повномасштабного вторгнення:\t{delta.days}🕊\n'
        f'Днів Соборності України:\t{days_of_unity.days}🤝'
    )

    anniversary = time.localtime().tm_year - 1919

    if time.localtime().tm_mon == 1 and time.localtime().tm_mday == 22:
        await message.answer(f'УРАААА, {anniversary} РІЧНИЦЯ СОБОРНОСТІ УКРАЇНИ')


@dp.message_handler(commands=['sticker'])
async def get_sticker(message: types.Message):
    data = extract_random_data.get_sticker()
    await bot.send_sticker(message.chat.id, sticker=f'{extract_random_data.get_random_sticker(data)}')
    await message.delete()


@dp.message_handler(commands=['currency'])
async def exchange_rate(message: types.Message):
    await bot.send_message(message.chat.id, 'Тут буде конвертер валют💵')


@dp.message_handler(regexp='sophie|sofiia|sofi|софі|софи')
async def call_sofi(message: types.Message):
    for i in range(0, 5):
        user_id = 639092726
        user_name = 'SOFI'
        mention = '[' + user_name + '](tg://user?id=' + str(user_id) + ')'
        bot_msg = f'WAKE UP, {mention}!!!'
        await bot.send_message(message.chat.id, bot_msg, parse_mode='Markdown')


@dp.message_handler(regexp='location|місцезнаходження')
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(content_types=['photo'], regexp='мем|mem')
async def create_mem(message: types.Message):
    await message.photo[-1].download('img/test.jpg')
    create_meme.create_meme()
    photo = InputFile("img/result.jpg")
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(regexp='martyn|мартин')
async def mention_bot(message: types.Message):
    data = extract_random_data.get_bullshit()
    await message.reply(f'{extract_random_data.get_random_data(data)}')


@dp.message_handler(regexp='аніме|берсєрк|бєрсєрк|берсерк')
async def mention_anime(message: types.Message):
    await message.reply('АНІМЕ - ГАВНО!!!💩💩💩')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
