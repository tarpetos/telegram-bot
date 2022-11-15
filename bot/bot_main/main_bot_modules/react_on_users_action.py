import os
from random import choice, randint

from aiogram import types
from aiogram.types import ContentType, InputFile

from bot.bot_main import main_objects_initialization
from bot.bot_main.for_mem_creation.create_meme import create_meme
from bot.bot_main.main_objects_initialization import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO, regexp='мем|mem')
async def create_mem(message: types.Message):
    await message.photo[-1].download('img/test.jpg')
    print('Photo downloaded...')
    create_meme(main_objects_initialization.extract_random_data.get_bullshit())
    photo = InputFile('img/result.jpg')
    print('Photo sending...')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(content_types=ContentType.VOICE)
async def voice_reply(message: types.Message):
    voice = InputFile(f'voice/{choice(os.listdir("voice"))}')

    print('Voice sending...')
    if randint(0, 5) == 3:
        print('Voice message answer are sending...')
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
