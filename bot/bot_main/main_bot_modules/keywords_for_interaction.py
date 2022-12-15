from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InputFile

from bot.bot_main import main_objects_initialization
from bot.bot_main.bot_classes.UserSticker import UserSticker
from bot.bot_main.for_photo_creation.remake_user_photo import create_new_photo_auto_config
from bot.other_functions import currency_cost as cc
from bot.bot_main.main_objects_initialization import dp, sticker_table, bot
from bot.other_functions.non_admin_message_filter import delete_non_admin_message
from bot.other_functions.remove_start_keyword import remove_mem_from_start


@dp.message_handler(regexp='^location$|^місцезнаходження$')
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(regexp='^bitcoin$|^біткоін$|^біток$')
async def bitcoin_price(message: types.Message):
    await message.reply(
        f'<b>Bitcoin price right now:</b> <span class="tg-spoiler">{cc.bitcoin_price()} $</span>\n', parse_mode='HTML'
    )


@dp.message_handler(regexp='^dtr sticker$|^дтр стікер$')
async def handle_message(message: types.Message):
    await UserSticker.user_sticker.set()
    await message.reply(
        'Send me a sticker and I will save it to database.'
        'Then you can use stickers by typing command /sticker.'
    )


@dp.message_handler(regexp='^dtr example$|^дтр приклад$')
async def help_with_photo(message: types.Message):
    await message.reply(
        '<b><i>Below you can see examples how to use command</i></b> /photo\n\n'
        '<code>example</code> - only one argument. Text "example" '
        'will be printed in the top left corner, font size = 20.\n'
        '<code>example//40</code> - two arguments. Text "example" '
        'will be printed in the top left corner, font size = 40.\n'
        '<code>100//200</code> - two arguments.  Resize photo: width = 100, height = 200\n'
        '<code>example//100//200</code> - three arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200, font size = 20.\n'
        '<code>example//100//200//40</code> - four arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200, font size = 40.\n'
        '<code>example//100//200//1000//2000//50</code> - six arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200. New width will be equal to 1000 and height - 2000, font size = 50.\n',
        parse_mode='HTML'
    )

@dp.message_handler(state=UserSticker.user_sticker, content_types=ContentType.STICKER)
async def create_photo(message: types.Message, state: FSMContext):
    sended_user_sticker = message.sticker.file_id
    print(sended_user_sticker)
    sticker_table.insert_into_sticker_table(sended_user_sticker)
    await message.reply(f'Your sticker was added successfully!')
    await state.finish()


@dp.message_handler(regexp='^mem|^мем', content_types=ContentType.PHOTO)
async def send_auto_config_photo_with_text(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file='imgs/test_auto_conf.jpg')
    get_user_photo_caption = message.caption
    formatted_text = remove_mem_from_start(get_user_photo_caption)

    create_new_photo_auto_config(formatted_text)

    result_photo = InputFile('imgs/result_auto_conf.jpg')
    await bot.send_photo(message.chat.id, photo=result_photo)


# @dp.message_handler(content_types=ContentType.VOICE)
# async def delete_all_except_admins(message: types.Message):
#     await delete_non_admin_message(message)
#
#
# @dp.message_handler(content_types=ContentType.VIDEO_NOTE)
# async def delete_all_except_admins(message: types.Message):
#     await delete_non_admin_message(message)


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
    print('Message text:', message.text)
    print('Message type:', message.content_type)
    print('Chat type:', message.chat.type)
    print('Message caption', message.caption, '\n')

    if username is None:
        username = ' '

    if full_name is None:
        full_name = ' '

    main_objects_initialization.store_users_data.connect_to_db(user_id, username, full_name, chat_id)
