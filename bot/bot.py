import random
import time
import extract_random_data
import create_meme

from aiogram.types import InputFile
from aiogram.utils import exceptions
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


# @dp.message_handler(regexp='photo')
# async def send_image(message: types.Message):
#     photo = InputFile("img/test.jpg")
#     await bot.send_photo(message.chat.id, photo=photo)


# @dp.message_handler(regexp='шо робите|вставайте|ну шо там')
# async def call_sofi(message: types.Message):
#     # Софі
#     user_sofi_id = 639092726
#     user_sofi_name = 'СОФІ'
#     mention_sofi = '[' + user_sofi_name + '](tg://user?id=' + str(user_sofi_id) + ')'
#
#     # Тарпетос
#     user_tarpetos_id = 441547155
#     user_tarpetos_name = 'ТАРАС'
#     mention_tarpetos = '[' + user_tarpetos_name + '](tg://user?id=' + str(user_tarpetos_id) + ')'
#
#     # Гігос
#     user_gigos_id = 420823189
#     user_gigos_name = 'МИРИК'
#     mention_gigos = '[' + user_gigos_name + '](tg://user?id=' + str(user_gigos_id) + ')'
#
#     # Євген @ost_adm
#     user_eugene_id = '@ost_adm'
#     user_eugene_name = 'ЖЕНЯ'
#     mention_eugene = '[' + user_eugene_name + '](tg://user?id=' + str(user_eugene_id) + ')'
#
#     # Влад
#     user_vlad_id = 922145120
#     user_vlad_name = 'ВЛАД'
#     mention_vlad = '[' + user_vlad_name + '](tg://user?id=' + str(user_vlad_id) + ')'
#
#     # Корнєй
#     user_korn_id = 867324388
#     user_korn_name = 'КОРНЄЙ'
#     mention_korn = '[' + user_korn_name + '](tg://user?id=' + str(user_korn_id) + ')'
#
#     # Кошик @kosh1kkk
#     user_artem_id = 891849290
#     user_artem_name = 'КОШИК'
#     mention_artem = '[' + user_artem_name + '](tg://user?id=' + str(user_artem_id) + ')'
#
#     # Даня @dan1sssimo
#     user_danya_id = 685244760
#     user_danya_name = 'ДАНЯ'
#     mention_danya = '[' + user_danya_name + '](tg://user?id=' + str(user_danya_id) + ')'
#
#     # Діма
#     user_dima_id = 661245516
#     user_dima_name = 'ДІМА'
#     mention_dima = '[' + user_dima_name + '](tg://user?id=' + str(user_dima_id) + ')'
#
#     # Аня @anafaryniuk
#     user_ann_id = 111111
#     user_ann_name = 'АНЯ'
#     mention_ann = '[' + user_ann_name + '](tg://user?id=' + str(user_ann_id) + ')'
#
#     # Ярик
#     user_yar_id = 881067050
#     user_yar_name = 'ЯРИК'
#     mention_yar = '[' + user_yar_name + '](tg://user?id=' + str(user_yar_id) + ')'
#
#     # bot_msg = f'АААААААААААААА СУКААААААА, ' \
#     #           f'{mention_tarpetos}, ' \
#     #           f'{mention_gigos}, ' \
#     #           f'{mention_vlad}, ' \
#     #           f'{mention_yar}, ' \
#     #           f'{mention_danya}, ' \
#     #           f'{mention_sofi}, ' \
#     #           f'{mention_dima}, ' \
#     #           f'{mention_ann}, ' \
#     #           f'{mention_eugene}, ' \
#     #           f'{mention_artem}, ' \
#     #           f'{mention_korn}!!! '
#
#     # bot_msg = f'АААААААААААААА СУКААААААА, {mention_tarpetos}, @anafaryniuk'
#
#     bot_msg = f'{mention_tarpetos}, ' \
#               f'{mention_gigos}, ' \
#               f'{mention_vlad}, ' \
#               f'{mention_dima}, ' \
#               f'{mention_sofi}, ' \
#               f'{mention_korn},' \
#               f'{mention_artem}, ' \
#               f'{mention_yar} (да, я знаю, шо це згадування не робить)'
#
#     await bot.send_message(message.chat.id, 'ААААААААААААААААААААААААААА', parse_mode='Markdown')
#     await bot.send_message(message.chat.id, bot_msg, parse_mode='Markdown')
#     await bot.send_message(message.chat.id, '@dan1sssimo, @anafaryniuk, @ost_adm')


@dp.message_handler(regexp='martyn|мартин')
async def mention_bot(message: types.Message):
    data = extract_random_data.get_bullshit()
    await message.reply(f'{extract_random_data.get_random_data(data)}')


@dp.message_handler(regexp='аніме|берсєрк|бєрсєрк|берсерк')
async def mention_anime(message: types.Message):
    await message.reply('АНІМЕ - ГАВНО!!!💩💩💩')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
