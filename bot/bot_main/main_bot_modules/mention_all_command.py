from aiogram import types

from bot.bot_main.main_objects_initialization import bot, dp


@dp.message_handler(commands=['all'])
async def call_all(message: types.Message):
    user_id_list = [
        395897536,
        661245516,
        441547155,
        639092726,
        881067050,
        891849290,
        922145120,
        420823189,
        428566833,
        867324388,
        685244760
    ]

    bot_msg = ''.join(
        '[' + str(i + 1) + '](tg://user?id=' + str(result) + ') '
        for i, result in enumerate(user_id_list)
    )

    await bot.send_message(message.chat.id, bot_msg, parse_mode='Markdown')
