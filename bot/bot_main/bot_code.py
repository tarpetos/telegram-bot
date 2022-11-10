import os
import re
import time
from datetime import date, datetime
from random import randint, choice

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import IsReplyFilter, Text
from aiogram.types import InputFile, ContentType, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData

from bot import parse_link
from bot import currency_cost as cc
from bot.bot_main.bot_classes.ConverterForm import ConverterForm
from bot.bot_main.bot_classes.DaysToBirthday import DaysToBirthday
from bot.bot_main.bot_classes.WeatherInfo import WeatherInfo
from bot.bot_main.bot_classes.SearchTerm import SearchTerm
from bot.bot_main.config import API_TOKEN, COMMANDS_LIST
from bot.bot_main.for_mem_creation.create_meme import create_meme
from bot.bot_main.for_mem_creation.extract_random_data import get_sticker, get_conversation_data, get_random_data
from bot.keyboards import converter_keyboard, currency_keyboard, random_numbers_keyboard
from bot.parse_temprature import parse_temp_at_time, parse_avarage_precipitation_probability, \
    parse_minmax_temp, find_avarage_temp_between_two, avarage_day_temp

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('ШТУЧНИЙ ІНТЕЛЕКТ ДТР-1')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=COMMANDS_LIST)


@dp.message_handler(commands=['random'])
async def randomize(message: types.Message):
    await message.reply('Виберіть діапазон числа:', reply_markup=random_numbers_keyboard.random_number_keyboard)


@dp.callback_query_handler(text=['random_value_1', 'random_value_2', 'random_value_3', 'random_value_4'])
async def choose_random(call: types.CallbackQuery):
    if call.data == 'random_value_1':
        await call.message.answer(
            f'Згенероване випадкове число: <code>{randint(0, 10)}</code> 🎲',
            parse_mode='HTML'
        )
    elif call.data == 'random_value_2':
        await call.message.answer(
            f'Згенероване випадкове число: <code>{randint(0, 100)}</code> 🎲',
            parse_mode='HTML')
    elif call.data == 'random_value_3':
        await call.message.answer(
            f'Згенероване випадкове число: <code>{randint(-100, 100)}</code> 🎲',
            parse_mode='HTML'
        )
    elif call.data == 'random_value_4':
        await call.message.answer(
            f'Згенероване випадкове число: <code>{randint(-1000000, 1000000)}</code> 🎲',
            parse_mode='HTML'
        )

    await call.answer()


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    await message.reply('Виберіть опцію меню💵:', reply_markup=currency_keyboard.currency_keyboard)


@dp.callback_query_handler(text=['currency_rate'])
async def exchange_rate(call: types.CallbackQuery):
    await call.message.answer(
        f'<b><i>КУПІВЛЯ / ПРОДАЖ</i></b>\n'
        f'<code>'
        f'1 гривня = {cc.find_dollars_buy_in_hryvnias():.4f} / {cc.find_dollars_sale_in_hryvnias():.4f} долара\n'
        f'1 гривня = {cc.find_euros_buy_in_hryvnias():.4f} / {cc.find_euros_sale_in_hryvnias():.4f} євро\n'
        f'1 євро   = {cc.find_dollars_buy_in_euros():.4f} / {cc.find_dollars_sale_in_euros():.4f} долара\n'
        f'1 євро   = {cc.find_hryvnias_buy_in_euros():.4f} / {cc.find_hryvnias_sale_in_euros():.4f} гривень\n'
        f'1 долар  = {cc.find_euros_buy_in_dollars():.4f} / {cc.find_euros_sale_in_dollars():.4f} євро\n'
        f'1 долар  = {cc.find_hryvnias_buy_in_dollars():.4f} / {cc.find_hryvnias_sale_in_dollars():.4f} гривень'
        f'</code>', parse_mode='HTML', reply_markup=ReplyKeyboardRemove()
    )
    await call.answer()


@dp.callback_query_handler(text=['currency_converter'])
async def converter(call: types.CallbackQuery):
    await call.message.answer('Конвертер валют:', reply_markup=converter_keyboard.converter_keyboard)
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(text=['convert_dollar'])
async def convert_dollar(call: types.CallbackQuery):
    await ConverterForm.dollar.set()
    await call.message.answer('Введіть кількість $ для конвертування в євро та гривні...')
    await call.answer()


@dp.message_handler(state=ConverterForm.dollar)
async def process_dollar(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)

        await message.answer(
            f'Вартість покупки доларів в гривнях: '
            f'{answer / cc.find_dollars_buy_in_hryvnias():.4f}\n'
            f'Вартість продажі доларів в гривнях: '
            f'{answer / cc.find_dollars_sale_in_hryvnias():.4f}\n'
            f'Вартість покупки доларів в євро: '
            f'{answer / cc.find_dollars_buy_in_euros():.4f}\n'
            f'Вартість продажі доларів в євро: '
            f'{answer / cc.find_dollars_sale_in_euros():.4f}\n'
        )
    except ValueError:
        await message.answer('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['convert_euro'])
async def convert_euro(call: types.CallbackQuery):
    await ConverterForm.euro.set()
    await call.message.answer('Введіть кількість € для конвертування в долари та гривні...')
    await call.answer()


@dp.message_handler(state=ConverterForm.euro)
async def process_euro(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.answer(
            f'Вартість покупки євро в гривнях: '
            f'{answer / cc.find_euros_buy_in_hryvnias():.4f}\n'
            f'Вартість продажі євро в гривнях: '
            f'{answer / cc.find_euros_sale_in_hryvnias():.4f}\n'
            f'Вартість покупки євро в доларах: '
            f'{answer / cc.find_euros_buy_in_dollars():.4f}\n'
            f'Вартість продажі євро в доларах: '
            f'{answer / cc.find_euros_sale_in_dollars():.4f}\n'
        )
    except ValueError:
        await message.answer('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['convert_hryvnia'])
async def convert_hryvnia(call: types.CallbackQuery):
    await ConverterForm.hryvnia.set()
    await call.message.answer('Введіть кількість ₴ для конвертування в долари та євро...')
    await call.answer()


@dp.message_handler(state=ConverterForm.hryvnia)
async def process_hryvnia(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(
            f'Вартість покупки гривні в доларах: '
            f'{answer / cc.find_hryvnias_buy_in_dollars():.4f}\n'
            f'Вартість продажі гривні в доларах: '
            f'{answer / cc.find_hryvnias_sale_in_dollars():.4f}\n'
            f'Вартість покупки гривні в євро: '
            f'{answer / cc.find_hryvnias_buy_in_euros():.4f}\n'
            f'Вартість продажі гривні в євро: '
            f'{answer / cc.find_hryvnias_sale_in_euros():.4f}\n'
        )
    except ValueError:
        await message.answer('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['back_to_menu'])
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.answer('Виберіть опцію меню💵:', reply_markup=currency_keyboard.currency_keyboard)
    await call.message.delete()
    await call.answer()


@dp.message_handler(commands=['id'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('ID', callback_data='user_id')
    keyboard_markup.row(user_id_btn)

    if message.from_user.username is not None:
        message.from_user.username = f'<code>{message.from_user.username}</code>'
    else:
        message.from_user.username = f'<span class="tg-spoiler"><b><i>користувач не має імені🤷</i></b></span>'

    await message.answer(
        f'Ім’я користувача: {message.from_user.username}\n'
        f'URL: {message.from_user.url}\n\n'
        'Натисни кнопку, щоб побачити свій ID...', parse_mode='HTML', reply_markup=keyboard_markup
    )

    await message.delete()


@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f'Ваш ID: {callback_query.from_user.id}', True)


@dp.message_handler(commands=['time'])
async def search_time(message: types.Message):
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    delta = date(current_year, current_month, current_day) - date(current_year, 2, 23)
    days_of_unity = date(current_year, current_month, current_day) - date(1919, 1, 21)

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

        await message.reply(f'Кількість днів між датами: {answer.days}')
    except ValueError:
        await message.reply('Дату вказано невірно.')

    await state.finish()


@dp.message_handler(commands=['sticker'])
async def choose_sticker(message: types.Message):
    data = get_sticker()
    await bot.send_sticker(message.chat.id, sticker=f'{get_random_data(data)}')
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
        temp_list = find_avarage_temp_between_two(url)
        await message.reply(
            f'{parse_temp_at_time(url)}\n\n'
            f'{parse_minmax_temp(url)}'
            f'{avarage_day_temp(url)}'
            f'Температура вночі: {temp_list[0]}\n'
            f'Температура зранку: {temp_list[1]}\n'
            f'Температура вдень: {temp_list[2]}\n'
            f'Температура ввечері: {temp_list[3]}\n\n'
            f'Максимальна ймовірність опадів: {parse_avarage_precipitation_probability(url)}%'
        )
    else:
        await message.reply('Місто вказано невірно.')

    await state.finish()


@dp.message_handler(regexp=re.compile('^/eugene$|^/eugene@TarpetosBOT$'))
async def parse_links(message: types.Message):
    await SearchTerm.search_term.set()
    await message.answer('Введіть ключові слова для пошуку відео...')


@dp.message_handler(state=SearchTerm.search_term)
async def process_links(message: types.Message, state: FSMContext):
    input_data = message.text

    print(input_data)
    try:
        answer = parse_link.links_split(input_data)

        result = ''
        for i in range(0, 5):
            result += f'{answer[i]}\n'

        await message.reply(f'{result}')
    except ValueError:
        await message.answer('По заданому запиту не вдалось знайти посилання.')

    await state.finish()


@dp.message_handler(regexp='здоров мартин|мартин здоров|мартинко здоров|привіт мартин|мартин привіт|мартинко привіт')
async def reply_on_hello(message: types.Message):
    answer_list = [
        'Здоров',
        'Привіт',
        'Хай',
        'Ку',
        'Hello',
        'Здоровенькі були',
    ]
    await message.reply(choice(answer_list))


@dp.message_handler(regexp='пока мартин|мартин пока|мартинко пока|бувай мартин|мартин бувай|мартинко бувай')
async def reply_on_goodbuy(message: types.Message):
    answer_list = [
        'Пока',
        'Бувай',
        'До побачення',
        'Будь здоров',
        'До зустрічі',
        'Надіюсь ми більше не зустрінемось',
    ]
    await message.reply(choice(answer_list))


@dp.message_handler(regexp='як справи мартин|мартин як справи|мартинко як справи|як діла мартин|мартин як '
                           'діла|мартинко як діла')
async def reply_on_goodbuy(message: types.Message):
    answer_list = [
        'Добре',
        'Норм',
        'А шо?',
        'Тобі яке діло?',
        'Так собі',
        'Непогано',
    ]
    await message.reply(choice(answer_list))


@dp.message_handler(regexp='стрємоус|спєрмоус|спермоус')
async def mention_putin(message: types.Message):
    answer_list = [
        'ЗДОХ. АХХАХАХАХА🎉🎉🎂🥳🎂🎉🎉\nВІТАЄМО ЙОГО!!!👏👏👏',
        'АЗАЗАЗ. ПАВ ДЕБІЛ😃😃😃',
        'В ГРОБ НАХУЙ!!!⚰⚰⚰',
        'ЛЕЖАААТИ, СПЄРМОУСОВ!!!🤣',
        'ПОМЕР. ІХІХІХІХ.😄😄😄',
    ]
    await message.reply(choice(answer_list))
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGXHdja6q6_5j6cXxfhfhXehxhG9tk8AACcBAAAgNXCEkOW0xbCSyuCCsE')


@dp.message_handler(IsReplyFilter(True))
async def reply_on_reply(message: types.Message):
    if message.reply_to_message.from_user.id == bot.id:
        if len(message.text) > 3 and message.text.endswith('?'):
            answer_list = [
                'Не знаю.',
                'В мене немає відповіді на це запитання.',
                'Ймовірно, що так.',
                'Так.',
                'Ні.',
                'Питання не зрозуміле.',
                'Ти задаєш якісь дивні запитання.',
                'Я не хочу відповідати на це.',
                'Більшість за все, що так.',
                'Да, єто так.',
                'Нічо',
                'Нічо, а шо.',
                'Нє, а шо.',
                'Сам такий.',
                'Добре',
                'Зрозумів',
                'Ок',
                'Я хачу пітси',
                'Пішов нахуй',
                'Де?',
                'Соси хуя',
            ]
            await message.reply(choice(answer_list))
        else:
            data = get_conversation_data()
            await message.reply(f'{get_random_data(data)}')


@dp.message_handler(content_types=ContentType.PHOTO, regexp='мем|mem')
async def create_mem(message: types.Message):
    await message.photo[-1].download('img/test.jpg')
    print('Photo downloaded...')
    create_meme()
    photo = InputFile('img/result.jpg')
    print('Photo sending...')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(content_types=ContentType.VOICE)
async def voice_reply(message: types.Message):
    voice = InputFile(f'voice/{choice(os.listdir("voice"))}')

    print('Voice sending...')
    if randint(0, 5) == 3:
        print('Voice message are sending...')
        await message.reply_voice(voice=voice)


@dp.message_handler(content_types=ContentType.LEFT_CHAT_MEMBER)
async def say_goodbye(message: types.Message):
    await message.reply('Пока👋')


@dp.message_handler(content_types=ContentType.NEW_CHAT_MEMBERS)
async def say_hello(message: types.Message):
    await message.reply('Здоров👋')


@dp.message_handler(content_types=ContentType.NEW_CHAT_PHOTO)
async def new_chat_photo(message: types.Message):
    await message.reply('О, нова фотка чату!')


@dp.message_handler(content_types=ContentType.DELETE_CHAT_PHOTO)
async def delete_chat_photo(message: types.Message):
    await message.reply('Знесли фотку чату. І шо буде далі? Державний переворт?')


@dp.message_handler(content_types=ContentType.VIDEO)
async def react_to_video(message: types.Message):
    react_list = [
        'Ну кинув відос. А тепер розкажи-но, шо там. Який зміст і тема відео?',
        'Шо за відос?',
        'Відос...ясно',
        'Не хочеш розказати, шо в відосі?',
    ]
    await message.reply(choice(react_list))


@dp.message_handler(content_types=ContentType.ANIMATION)
async def react_to_animation(message: types.Message):
    react_list = [
        'Шо це? Гіфка? Я таке не читаю',
        'Ймовірно, колись творець навчить мене розуміти це',
        'Не люблю я таких файлів.',
        'Чи нема там мему випадково?',
        'Пропоную вирізати з цього файлу фото і надіслати мені з підписом "мем".',
    ]
    await message.reply(choice(react_list))


@dp.message_handler(content_types=ContentType.POLL)
async def react_to_poll(message: types.Message):
    await message.reply('Розкажіть, про шо голосування Мартину')


@dp.message_handler(regexp='location|місцезнаходження')
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(regexp='аніме|берсєрк|бєрсєрк|берсерк|человек бензопила|чєловєк бензопила')
async def mention_anime(message: types.Message):
    await message.reply('АНІМЕ - ГАВНО!!!💩💩💩')


@dp.message_handler(regexp='martyn|мартин|дтр')
async def mention_bot(message: types.Message):
    data = get_conversation_data()
    await message.reply(f'{get_random_data(data)}')


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


@dp.message_handler(regexp='бравл|brawl')
async def mention_putin(message: types.Message):
    await message.reply('БРАВЛІК - ХУЯВЛІК')


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
    await message.reply(
        f'<b>Вартість Bitcoin зараз.</b>\n\n'
        f'Купівля: <span class="tg-spoiler">{cc.bitcoin_buy()} $</span>\n'
        f'Продаж: <span class="tg-spoiler">{cc.bitcoin_sale()} $</span>', parse_mode='HTML'
    )


@dp.message_handler(content_types=ContentType.TEXT)
async def call_sofi_again(message: types.Message):
    answer_probability = randint(1, 50)

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

    await check_bot_usage(message)


@dp.message_handler(content_types=ContentType.ANY)
async def check_bot_usage(message: types.Message):
    print('Message chat id:', message.chat.id)
    print('Bot id:', message.bot.id)
    print('From what id message:', message.from_id)
    print('Message id:', message.message_id, '\n')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
