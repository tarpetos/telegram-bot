import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main.bot_classes.WeatherInfo import WeatherInfo
from bot.bot_main.main_objects_initialization import dp
from bot.parsing.parse_temprature import find_avarage_temp_between_two, parse_temp_at_time, parse_minmax_temp, \
    avarage_day_temp, parse_avarage_precipitation_probability


@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    await WeatherInfo.place.set()
    await message.reply('Введіть назву міста...')


@dp.message_handler(state=WeatherInfo.place)
async def process_weather(message: types.Message, state: FSMContext):
    input_place = message.text

    url = f'https://ua.sinoptik.ua/погода-{input_place}'
    answer = requests.get(url)

    if answer.status_code == 200:
        temp_list = find_avarage_temp_between_two(url)
        await message.reply(
            f'{parse_temp_at_time(url)}\n\n'
            f'{parse_minmax_temp(url)}'
            f'{avarage_day_temp(url)}'
            f'Температура вночі: {temp_list[0]}\n'
            f'Температура зранку: {temp_list[1]}\n'
            f'Температура вдень: {temp_list[2]}\n'
            f'Температура ввечері: {temp_list[3]}\n\n'
            f'Максимальна ймовірність опадів: {parse_avarage_precipitation_probability(url)}%',
            parse_mode='Markdown'
        )
    else:
        await message.reply('Місто вказано невірно.')

    await state.finish()
