import time
from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext

from .commands_utils.states import DaysToBirthday
from ..config import dp
from ..enums import Command
from bot.keywords.keyword_utils.check_date_words import check_year, check_month, check_day


@dp.message_handler(state="*", commands=Command.DATE_CALCULATOR)
async def date_calculator_command_handler(message: types.Message):
    await DaysToBirthday.day_month.set()
    await message.reply("Enter date of birth (or other date) in format dd.mm.yyyy...")


@dp.message_handler(state=DaysToBirthday.day_month)
async def process_date_calculator_command(message: types.Message, state: FSMContext):
    input_data = message.text
    input_data = input_data.split(".", 2)
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    try:
        answer = abs(
            date(current_year, current_month, current_day)
            - date(int(input_data[2]), int(input_data[1]), int(input_data[0]))
        )

        years = int(answer.days / 365)
        months = int((answer.days % 365) / 31)
        days = answer.days - years * 365 - months * 31
        await message.reply(
            f"The number of days between the entered date and the current date: {answer.days}\n"
            f"Formatted date: "
            f"{years} {check_year(years)}, {months} {check_month(months)}, {days} {check_day(days)}"
        )
    except ValueError:
        await message.reply("Your input was incorrect! Try again.")
    except IndexError:
        await message.reply("Your input was incorrect! Try again.")

    await state.finish()
