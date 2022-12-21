from aiogram import types

from bot.bot_main.main_objects_initialization import dp


@dp.message_handler(commands=['keywords'])
async def get_keywords(message: types.Message):
    await message.reply(
        # '<code>martyn</code> — <i>get random message from bot</i>\n'
        '<code>location</code> — <i>get bot location</i>\n\n'
        
        '<code>bitcoin</code> — <i>get bitcoin price</i>\n\n'
        
        '<code>dtr sticker</code> — <i>add your sticker to bot database</i>\n\n'
        
        '<code>dtr example</code> — <i>send you few examples how to use</i> /photo\n\n'
        
        '<code>mem any_text</code> — <i>send me an image with caption where must be word</i> <b>"mem"</b> '
        '<i>and after this word you can type anything. All what you will type after keyword will be printed '
        'on your image and sent to you</i>\n\n'
        
        '<code>What date will it be after N days?</code> — <i>send you a message with a date that will '
        'be after</i> <b>N</b> <i>days from the current date in format</i> <b>dd.mm.yyyy</b>\n\n'
        
        '<code>What date will be after N days if we start from "your_date"?</code> — <i>send you a message with a date '
        'that will be after</i> <b>N</b> <i>days from</i> <b>"your_date"</b> '
        '<i>(must be in the same format as in the result) in format</i> <b>dd.mm.yyyy</b>\n\n',
        parse_mode='HTML'
    )
