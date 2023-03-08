from aiogram import types

from bot.bot_main.main_objects_initialization import dp


@dp.message_handler(state='*', commands=['keywords'])
async def get_keywords(message: types.Message):
    await message.reply(
        '<code>bitcoin</code> — <i>get bitcoin price</i>\n\n'
        
        '<code>dtr sticker</code> — <i>add your sticker to bot database</i>\n\n'
        
        '<code>dtr example</code> — <i>send you few examples how to use</i> /photo\n\n'
        
        '<code>msgd</code> — <i>deletes the bot message you replied to and your message</i>\n\n'
        
        '<code>random mem any_text</code> — <i>send me an image with caption where must be words</i> <b>"random mem"</b> '
        '<i>and after this words you can type anything. All what you will type after keyword will be printed '
        'on your image and sent to you back. Font color will be randomly generated.</i>\n\n'
        
        '<code>mem any_text</code> — <i>send me an image with caption where must be word</i> <b>"mem"</b> '
        '<i>and after this word you can type anything. All what you will type after keyword will be printed '
        'on your image and sent to you. Font color for the image will be automatically set by the system '
        'depending on the colors that the image contains.</i>\n\n'
        
        '<code>What date will it be after N days?</code> — <i>send you a message with a date that will '
        'be after</i> <b>N</b> <i>days from the current date in format</i> <b>dd.mm.yyyy</b>\n\n'
        
        '<code>What date will be after N days if we start from "your_date"?</code> — <i>send you a message with a date '
        'that will be after</i> <b>N</b> <i>days from</i> <b>"your_date"</b> '
        '<i>(must be in the same format as in the result) in format</i> <b>dd.mm.yyyy</b>\n\n'
        
        '<code>dtr delete tasks</code> — <i>deletes the table and all its contents created using the command</i> '
        '/taskscheduler <i>and creates a new empty task table</i>\n\n'

        '<code>dtr delete passwords</code> — <i>deletes the table and all its contents created using the command</i> '
        '/password <i>and creates a new empty password table</i>\n\n',
        parse_mode='HTML'
    )
