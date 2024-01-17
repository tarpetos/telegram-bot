from datetime import date, datetime
from aiogram import types

from ..config import dp
from ..enums import Command


@dp.message_handler(state="*", commands=Command.TIME)
async def time_command_handler(message: types.Message):
    utc_time = datetime.utcnow()
    current_year = utc_time.timetuple().tm_year
    current_month = utc_time.timetuple().tm_mon
    current_day = utc_time.timetuple().tm_mday

    delta = date(current_year, current_month, current_day) - date(2022, 2, 24)
    days_of_unity = date(current_year, current_month, current_day) - date(1919, 1, 21)

    await message.reply(
        f'Current date:\t{utc_time.strftime("%d.%m.%Y UTC")} 📅\n'
        f'Current time:\t{utc_time.strftime("%H:%M:%S UTC")} 🕔\n'
        f'Day of the week:\t{(utc_time.strftime("%A")).upper()}\n'
        f"Day of the year:\t{utc_time.timetuple().tm_yday} 🌞\n"
        f"Number of days after russian full scale invasion to Ukraine:\t{delta.days + 1} 🕊\n"
        f"Day of Unity of Ukraine:\t{days_of_unity.days} 🤝"
    )

    if current_month == 1 and current_day == 22:
        anniversary = current_year - 1919
        await message.answer(
            f"WOW, {anniversary}TH ANNIVERSARY OF THE UNITY OF UKRAINE"
        )
