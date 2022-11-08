import time
import os
import extract_random_data
import create_meme

from parse_temprature import *
from currency_cost import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from converter_keyboard import converter_keyboard
from currency_keyboard import currency_keyboard
from random_numbers_keyboard import keyboard_random
from random import randint, choice
from aiogram.types import InputFile, ContentType, ReplyKeyboardRemove
from config import API_TOKEN, COMMANDS_LIST
from datetime import date
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class ConverterForm(StatesGroup):
    dollar = State()
    euro = State()
    hryvnia = State()


class WeatherInfo(StatesGroup):
    place = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('ШТУЧНИЙ ІНТЕЛЕКТ ДТР-1')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=COMMANDS_LIST)
    await message.delete()


@dp.message_handler(commands=['random'])
async def randomize(message: types.Message):
    await message.reply('Виберіть діапазон числа:', reply_markup=keyboard_random)


@dp.callback_query_handler(text=['random_value_1', 'random_value_2', 'random_value_3', 'random_value_4'])
async def choose_random(call: types.CallbackQuery):
    if call.data == 'random_value_1':
        await call.message.answer(f'Згенероване випадкове число: <code>{randint(0, 10)}</code> 🎲',
                                  parse_mode='HTML')
    elif call.data == 'random_value_2':
        await call.message.answer(f'Згенероване випадкове число: <code>{randint(0, 100)}</code> 🎲',
                                  parse_mode='HTML')
    elif call.data == 'random_value_3':
        await call.message.answer(f'Згенероване випадкове число: <code>{randint(-100, 100)}</code> 🎲',
                                  parse_mode='HTML')
    elif call.data == 'random_value_4':
        await call.message.answer(f'Згенероване випадкове число: <code>{randint(-1000000, 1000000)}</code> 🎲',
                                  parse_mode='HTML')

    await call.answer()


@dp.message_handler(commands=['eugene'])
async def mark_eugene(message: types.Message):
    await message.reply('Команда "eugene" тимчасово не працює.🤷‍')


@dp.message_handler(commands=['id'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('ID', callback_data='user_id')
    keyboard_markup.row(user_id_btn)

    if message.from_user.username is not None:
        message.from_user.username = f'<code>{message.from_user.username}</code>'
    else:
        message.from_user.username = f'<span class="tg-spoiler"><b><i>користувач не має імені🤷</i></b></span>'

    await message.answer(f'Ім’я користувача: {message.from_user.username}\n'
                         f'URL: {message.from_user.url}\n\n'
                         'Натисни кнопку, щоб побачити свій ID...', parse_mode='HTML', reply_markup=keyboard_markup)

    await message.delete()


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
    await bot.send_sticker(message.chat.id, sticker=f'{extract_random_data.get_random_data(data)}')
    await message.delete()


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
        temp_list = parse_today_temp(url)
        await message.reply(f'Середня температура сьогодні: {parse_avarage_today_temp(url)}\n\n'
                            f'Температура вночі: {temp_list[0][0]}\n'
                            f'Температура зранку: {temp_list[1][0]}\n'
                            f'Температура вдень: {temp_list[2][0]}\n'
                            f'Температура ввечері: {temp_list[3][0]}\n\n'
                            f'Максимальна ймовірність опадів: {parse_avarage_precipitation_probability(url)}%')
    else:
        await message.reply('Місто вказано невірно.')

    await state.finish()


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    await bot.send_message(message.chat.id, 'Відкрито конвертер валют💵', reply_markup=currency_keyboard)


@dp.message_handler(Text(equals='Курс валют'))
async def exchange_rate(message: types.Message):
    await message.answer(f'<b><i>КУПІВЛЯ / ПРОДАЖ</i></b>\n'
                         f'<code>'
                         f'1 гривня = {find_dollars_buy_in_hryvnias()} / {find_dollars_sale_in_hryvnias()} долара\n'
                         f'1 гривня = {find_euros_buy_in_hryvnias()} / {find_euros_sale_in_hryvnias()} євро\n'
                         f'1 євро   = {find_dollars_buy_in_euros()} / {find_dollars_sale_in_euros()} долара\n'
                         f'1 євро   = {find_hryvnias_buy_in_euros()} / {find_hryvnias_sale_in_euros()} гривень\n'
                         f'1 долар  = {find_euros_buy_in_dollars()} / {find_euros_sale_in_dollars()} євро\n'
                         f'1 долар  = {find_hryvnias_buy_in_dollars()} / {find_hryvnias_sale_in_dollars()} гривень'
                         f'</code>', parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals='Конвертація'))
async def converter(message: types.Message):
    await bot.send_message(message.chat.id, 'Конвертер валют', reply_markup=converter_keyboard)
    await message.delete()


@dp.message_handler(Text(equals='Конвертація долара'))
async def convert_dollar(message: types.Message):
    await ConverterForm.dollar.set()
    await message.reply('Введіть кількість $ для конвертування в євро та гривні...')


@dp.message_handler(state=ConverterForm.dollar)
async def process_dollar(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(f'Вартість покупки доларів в гривнях: '
                            f'{format(answer / float(find_dollars_buy_in_hryvnias()), ".4f")}\n'
                            f'Вартість продажі доларів в гривнях: '
                            f'{format(answer / float(find_dollars_sale_in_hryvnias()), ".4f")}\n'
                            f'Вартість покупки доларів в євро: '
                            f'{format(answer / float(find_dollars_buy_in_euros()), ".4f")}\n'
                            f'Вартість продажі доларів в євро: '
                            f'{format(answer / float(find_dollars_sale_in_euros()), ".4f")}\n')
    except:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.message_handler(Text(equals='Конвертація євро'))
async def convert_euro(message: types.Message):
    await ConverterForm.euro.set()
    await message.reply('Введіть кількість € для конвертування в долари та гривні...')


@dp.message_handler(state=ConverterForm.euro)
async def process_euro(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(f'Вартість покупки євро в гривнях: '
                            f'{format(answer / float(find_euros_buy_in_hryvnias()), ".4f")}\n'
                            f'Вартість продажі євро в гривнях: '
                            f'{format(answer / float(find_euros_sale_in_hryvnias()), ".4f")}\n'
                            f'Вартість покупки євро в доларах: '
                            f'{format(answer / float(find_euros_buy_in_dollars()), ".4f")}\n'
                            f'Вартість продажі євро в доларах: '
                            f'{format(answer / float(find_euros_sale_in_dollars()), ".4f")}\n')
    except:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.message_handler(Text(equals='Конвертація гривні'))
async def convert_hryvnia(message: types.Message):
    await ConverterForm.hryvnia.set()
    await message.reply('Введіть кількість ₴ для конвертування в долари та євро...')


@dp.message_handler(state=ConverterForm.hryvnia)
async def process_hryvnia(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(f'Вартість покупки гривні в доларах: '
                            f'{format(answer / float(find_hryvnias_buy_in_dollars()), ".4f")}\n'
                            f'Вартість продажі гривні в доларах: '
                            f'{format(answer / float(find_hryvnias_sale_in_dollars()), ".4f")}\n'
                            f'Вартість покупки гривні в євро: '
                            f'{format(answer / float(find_hryvnias_buy_in_euros()), ".4f")}\n'
                            f'Вартість продажі гривні в євро: '
                            f'{format(answer / float(find_hryvnias_sale_in_euros()), ".4f")}\n')
    except:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.message_handler(Text(equals='До головного меню'))
async def back_to_main_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Перехід до головного меню конвертера...', reply_markup=currency_keyboard)
    await message.delete()


@dp.message_handler(Text(equals='Закрити клавіатуру'))
async def close_keyboard(message: types.Message):
    await bot.send_message(message.chat.id, 'Закриття клавіатури...', reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(content_types=ContentType.PHOTO, regexp='мем|mem')
async def create_mem(message: types.Message):
    await message.photo[-1].download('img/test.jpg')
    print('Photo downloaded...')
    create_meme.create_meme()
    photo = InputFile('img/result.jpg')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(content_types=ContentType.VOICE)
async def create_mem(message: types.Message):
    voice = InputFile(f'voice/{choice(os.listdir("voice"))}')

    if randint(0, 5) == 3:
        print('Voice message are sending...')
        await message.reply_voice(voice=voice)


@dp.message_handler(regexp='location|місцезнаходження')
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(regexp='аніме|берсєрк|бєрсєрк|берсерк')
async def mention_anime(message: types.Message):
    await message.reply('АНІМЕ - ГАВНО!!!💩💩💩')


@dp.message_handler(regexp='martyn|мартин|дтр')
async def mention_bot(message: types.Message):
    data = extract_random_data.get_conversation_data()
    await message.reply(f'{extract_random_data.get_random_data(data)}')


@dp.message_handler(regexp='слава україні|україні слава')
async def mention_glory(message: types.Message):
    await message.reply('ГЕРОЯМ СЛАВА!!!')


@dp.message_handler(regexp='слава нації')
async def mention_nation(message: types.Message):
    await message.reply('СМЕРТЬ ВОРОГАМ!!!')


@dp.message_handler(regexp='Україна')
async def mention_ukraine(message: types.Message):
    await message.reply('ПОНАД УСЕ!!!')


@dp.message_handler(regexp='путін|пиня|рєзіновая попа|рєзінавая попа|путя|пинька|putin')
async def mention_putin(message: types.Message):
    await message.reply('ХУЙЛО!!!')


@dp.message_handler(regexp='sophie|sofiia|sofi|софі|софи')
async def call_sofi(message: types.Message):
    for i in range(0, 5):
        user_id = 639092726
        user_name = 'SOFI'
        mention = '[' + user_name + '](tg://user?id=' + str(user_id) + ')'
        bot_msg = f'WAKE UP, {mention}!!!'
        await bot.send_message(message.chat.id, bot_msg, parse_mode='Markdown')


@dp.message_handler(regexp='bitcoin|біткоін|біток|по чому монєта|шо з монєтою|по чому монета|шо з монетою')
async def bitcoin_price(message: types.Message):
    await message.reply(f'<b>Вартість Bitcoin зараз.</b>\n\n'
                        f'Купівля: <span class="tg-spoiler">{bitcoin_buy()} $</span>\n'
                        f'Продаж: <span class="tg-spoiler">{bitcoin_sale()} $</span>', parse_mode='HTML')


@dp.message_handler(content_types=ContentType.TEXT)
async def call_sofi_again(message: types.Message):
    answer_probability = randint(1, 10)
    print(answer_probability)

    if answer_probability == 1:
        user_id = 639092726
        user_name = 'Софі'
        mention = '[' + user_name + '](tg://user?id=' + str(user_id) + ')'

        bot_msg = [
            f'Слуууухай...пора би підкачатись, {mention}!!!',
            f'Качалка це добре, {mention}!!!',
            f'Йди качай банки, {mention}!!!',
            f'Я б на твому місці підкачався, {mention}.',
            f'Не хочеш покачатись трохи, {mention}???',
            f'Я не можу качатись, бо я телеграм-бот, але ти може. Пора, {mention}!!!'
        ]

        await bot.send_message(message.chat.id, choice(bot_msg), parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
