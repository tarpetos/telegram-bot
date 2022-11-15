from random import choice, randint

from aiogram import types
from aiogram.dispatcher.filters import IsReplyFilter
from aiogram.types import ContentType

from bot.bot_main import main_objects_initialization
from bot.bot_main.for_mem_creation.extract_random_data import get_random_data
from bot.bot_main.main_objects_initialization import dp, bot


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
async def reply_on_goodbye(message: types.Message):
    answer_list = [
        'Пока',
        'Бувай',
        'До побачення',
        'Будь здоров',
        'До зустрічі',
        'Надіюсь ми більше не зустрінемось',
    ]
    await message.reply(choice(answer_list))


@dp.message_handler(
    regexp='як справи мартин|мартин як справи|мартинко як справи|як діла мартин|мартин як діла|мартинко як діла'
)
async def reply_on_how_are_you(message: types.Message):
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
async def mention_spermous(message: types.Message):
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
        if message.text.endswith('йди нахуй') or message.text.endswith('пішов нахуй') or \
                message.text.endswith('іди нахуй') or message.text.endswith('нахуй пішов') or \
                message.text.endswith('нахуй іди') or message.text.endswith('нахуй йди'):

            answer_list = [
                'сам йди нахуй',
                'ти йди нахуй',
                'нє, ти йди нахуй',
            ]
            await message.reply(choice(answer_list))
        elif len(message.text) > 3 and message.text.endswith('?'):
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
            data = main_objects_initialization.extract_random_data.get_conversation_data()
            await message.reply(f'{get_random_data(data)}')


@dp.message_handler(regexp='аніме|берсєрк|бєрсєрк|берсерк|человек бензопила|чєловєк бензопила')
async def mention_anime(message: types.Message):
    await message.reply('АНІМЕ - ГАВНО!!!💩💩💩')


@dp.message_handler(regexp='martyn|мартин|дтр')
async def mention_bot(message: types.Message):
    data = main_objects_initialization.extract_random_data.get_conversation_data()
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
async def mention_brawl(message: types.Message):
    await message.reply('БРАВЛІК - ХУЯВЛІК')


@dp.message_handler(regexp='sophie|sofiia|sofi|софі|софи')
async def call_sofi(message: types.Message):
    for i in range(0, 5):
        user_id = 639092726
        user_name = 'SOFI'
        mention = '[' + user_name + '](tg://user?id=' + str(user_id) + ')'
        bot_msg = f'WAKE UP, {mention}!!!'
        await bot.send_message(message.chat.id, bot_msg, parse_mode='Markdown')


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
    chat_id = message.chat.id
    bot_id = message.bot.id
    user_id = message.from_id
    username = message.from_user.username
    full_name = message.from_user.full_name
    message_id = message.message_id

    print('Message chat id:', chat_id)
    print('Bot id:', bot_id)
    print('From what id message:', user_id)
    print('From what username:', username)
    print('From user full name:', full_name)
    print('Message id:', message_id)
    print('Message text:', message.text, '\n')

    if username is None:
        username = ' '

    if full_name is None:
        full_name = ' '

    main_objects_initialization.store_users_data.connect_to_db(user_id, username, full_name, chat_id)
