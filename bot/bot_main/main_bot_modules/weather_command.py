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
    await message.reply('Enter the name of the town...')


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
            f'Night temrature: {temp_list[0]}\n'
            f'Morning temperature: {temp_list[1]}\n'
            f'Day temperature: {temp_list[2]}\n'
            f'Evening temperature: {temp_list[3]}\n\n'
            f'Maximum chance of precipitation: {parse_avarage_precipitation_probability(url)}%',
            parse_mode='Markdown'
        )
    else:
        await message.reply('Can not find such town name!')

    await state.finish()
