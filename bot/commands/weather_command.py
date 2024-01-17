import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from .commands_utils.states import WeatherInfo
from .commands_utils.parse_temprature import (
    find_average_temp_between_two,
    parse_minmax_temp,
    average_day_temp,
    parse_average_precipitation_probability,
)
from ..config import dp
from ..enums import Command


@dp.message_handler(state="*", commands=Command.CURRENT_WEATHER)
async def weather_command_handler(message: types.Message):
    await WeatherInfo.place.set()
    await message.reply("Enter the name of the town...")


@dp.message_handler(state=WeatherInfo.place)
async def process_weather_command(message: types.Message, state: FSMContext):
    input_place = message.text

    url = f"https://ua.sinoptik.ua/погода-{input_place}"
    answer = requests.get(url)

    if answer.status_code == 200:
        temp_list = find_average_temp_between_two(url)
        await message.reply(
            f"{parse_minmax_temp(url)}"
            f"{average_day_temp(url)}"
            f"Night temperature: {temp_list[0]}\n"
            f"Morning temperature: {temp_list[1]}\n"
            f"Day temperature: {temp_list[2]}\n"
            f"Evening temperature: {temp_list[3]}\n\n"
            f"Maximum chance of precipitation: {parse_average_precipitation_probability(url)}%",
            parse_mode="Markdown",
        )
    else:
        await message.reply("Can not find such town name!")

    await state.finish()
