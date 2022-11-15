import locale
import time
from datetime import date, datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main.bot_classes.DaysToBirthday import DaysToBirthday
from bot.bot_main.main_objects_initialization import dp
from bot.other_functions.check_date_words import check_year, check_month, check_day


@dp.message_handler(commands=['time'])
async def search_time(message: types.Message):
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    delta = date(current_year, current_month, current_day) - date(current_year, 2, 23)
    days_of_unity = date(current_year, current_month, current_day) - date(1919, 1, 21)

    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    await message.reply(
        f'Поточна дата:\t{datetime.now().strftime("%d.%m.%Y")}📅\n'
        f'Поточний час:\t{datetime.now().strftime("%H:%M:%S")}🕔\n'
        f'День тижня:\t{datetime.now().strftime("%A")}\n'
        f'День року:\t{time.localtime().tm_yday}🌞\n'
        f'К-сть днів з початку повномасштабного вторгнення:\t{delta.days}🕊\n'
        f'День Соборності України:\t{days_of_unity.days}🤝'
    )

    anniversary = time.localtime().tm_year - 1919

    if time.localtime().tm_mon == 1 and time.localtime().tm_mday == 22:
        await message.answer(f'УРАААА, {anniversary} РІЧНИЦЯ СОБОРНОСТІ УКРАЇНИ')


@dp.message_handler(commands=['birthday'])
async def get_birthday(message: types.Message):
    await DaysToBirthday.day_month.set()
    await message.reply('Введіть дату народження (або іншу дату) в форматі дд.мм.рррр...')


@dp.message_handler(state=DaysToBirthday.day_month)
async def process_birthday(message: types.Message, state: FSMContext):
    input_data = message.text
    input_data = input_data.split('.', 2)
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    try:
        answer = abs(
            date(current_year, current_month, current_day) -
            date(int(input_data[2]), int(input_data[1]), int(input_data[0]))
        )

        years = int(answer.days / 365)
        months = int((answer.days % 365) / 31)
        days = answer.days - years * 365 - months * 31
        await message.reply(f'Кількість днів між вказаною і поточною датою: {answer.days}\n'
                            f'Форматований запис: '
                            f'{years} {check_year(years)}, {months} {check_month(months)}, {days} {check_day(days)}')
    except ValueError:
        await message.reply('Дату вказано невірно.')

    await state.finish()
