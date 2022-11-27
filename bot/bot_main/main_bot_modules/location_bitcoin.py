from aiogram import types

from bot.bot_main.main_objects_initialization import dp, bot
from bot.other_functions import currency_cost as cc


@dp.message_handler(regexp='location|місцезнаходження')
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(regexp='bitcoin|біткоін|біток|по чому монєта|шо з монєтою|по чому монета|шо з монетою')
async def bitcoin_price(message: types.Message):
    await message.reply(
        f'<b>Вартість Bitcoin зараз:</b> <span class="tg-spoiler">{cc.bitcoin_price()} $</span>\n', parse_mode='HTML'
    )
