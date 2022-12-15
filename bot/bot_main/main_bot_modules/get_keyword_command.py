from aiogram import types

from bot.bot_main.main_objects_initialization import dp


@dp.message_handler(commands=['keywords'])
async def get_keywords(message: types.Message):
    await message.reply(
        # '<code>martyn</code> — <i>get random message from bot</i>\n'
        '<code>location</code> — <i>get bot location</i>\n'
        '<code>bitcoin</code> — <i>get bitcoin price</i>\n'
        '<code>dtr sticker</code> — <i>add your sticker to bot database</i>\n'
        '<code>dtr example</code> — <i>send you few examples how to use /photo</i>\n'
        '<code>mem any_text</code> — <i>send me an image with caption where must be word "mem" and after this word you '
        'can type anything. All what you will type after keyword will be printed on your image and sent to you</i>\n',
        parse_mode='HTML'
    )
