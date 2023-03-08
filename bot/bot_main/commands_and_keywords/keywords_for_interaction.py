import re
from datetime import datetime, timedelta

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import IsReplyFilter
from aiogram.types import ContentType, InputFile

from bot.bot_main.bot_classes.UserSticker import UserSticker
from bot.bot_main.for_photo_creation.remake_user_photo import create_new_photo_auto_config
from bot.other_functions import currency_cost as cc
from bot.bot_main.main_objects_initialization import dp, sticker_table, bot, unique_table, store_users_data
from bot.other_functions.check_date_words import check_day
from bot.other_functions.get_days_and_date_num import exctract_from_user_input_days_and_date, \
    exctract_from_user_input_days_num
# from bot.other_functions.non_admin_message_filter import delete_non_admin_message, get_admin_ids
from bot.other_functions.remove_start_keyword import remove_mem_from_start, remove_rand_mem_from_start


@dp.message_handler(regexp='^dtr delete tasks$|^дтр видали завдання$')
async def tasks_delete(message: types.Message):
    user_id = message.from_id
    unique_table.drop_remake_task_table(user_id)
    await message.reply(text='All tasks successfully deleted!!!')


@dp.message_handler(regexp='^dtr delete passwords$|^дтр видали паролі$')
async def passwords_delete(message: types.Message):
    user_id = message.from_id
    unique_table.drop_remake_password_table(user_id)
    await message.reply(text='All passwords successfully deleted!!!')


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
        'will be printed in the top left corner, font size = 20.\n\n'
        
        '<code>example//40</code> - two arguments. Text "example" '
        'will be printed in the top left corner, font size = 40.\n\n'
        
        '<code>100//200</code> - two arguments.  Resize photo: width = 100, height = 200\n\n'
        
        '<code>example//100//200</code> - three arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200, font size = 20.\n\n'
        
        '<code>example//100//200//40</code> - four arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200, font size = 40.\n\n'
        
        '<code>example//100//200//1000//2000//50</code> - six arguments. Text "example" '
        'will be printed in position where coordinate X = 100 '
        'and coordinate Y = 200. New width will be equal to 1000 and height - 2000, font size = 50.\n',
        parse_mode='HTML'
    )

@dp.message_handler(state=UserSticker.user_sticker, content_types=ContentType.STICKER)
async def create_photo(message: types.Message, state: FSMContext):
    sended_user_sticker = message.sticker.file_id
    sticker_table.insert_into_sticker_table(sended_user_sticker)
    await message.reply(f'Your sticker was added successfully!')
    await state.finish()


@dp.message_handler(regexp='^random mem|^рандом мем', content_types=ContentType.PHOTO)
async def send_auto_config_photo_with_rand_text_clr(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file='imgs/test_auto_conf.jpg')
    get_user_photo_caption = message.caption
    formatted_text = remove_rand_mem_from_start(get_user_photo_caption)

    create_new_photo_auto_config(False, formatted_text)

    result_photo = InputFile('imgs/result_auto_conf.jpg')
    await bot.send_photo(message.chat.id, photo=result_photo)


@dp.message_handler(regexp='^mem|^мем', content_types=ContentType.PHOTO)
async def send_auto_config_photo_with_text(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file='imgs/test_auto_conf.jpg')
    get_user_photo_caption = message.caption
    formatted_text = remove_mem_from_start(get_user_photo_caption)

    create_new_photo_auto_config(True, formatted_text)

    result_photo = InputFile('imgs/result_auto_conf.jpg')
    await bot.send_photo(message.chat.id, photo=result_photo)


@dp.message_handler(IsReplyFilter(True), regexp='^msgd$|пвдв$')
async def delete_two_messages(message: types.Message):
    if message.reply_to_message.from_user.id == bot.id:
        replied_msg_id = message.reply_to_message.message_id
        await bot.delete_message(chat_id=message.chat.id, message_id=replied_msg_id)
        await message.delete()
    else:
        return


@dp.message_handler(
    regexp=re.compile(
        '^(Яка дата|Який день) буде через [1-9]+[0-9]* (день|днів|дня)[?]*$|'
        '^What (date|day) will be after [1-9]+[0-9]* (day|days)[?]*$',
        re.IGNORECASE
    )
)
async def find_date_after_days_from_current_date(message: types.Message):
    user_input = message.text
    extracted_days = exctract_from_user_input_days_num(user_input)

    today = datetime.now()
    answer = today + timedelta(days=extracted_days)
    format_answer = answer.strftime('%d.%m.%Y')

    await message.reply(
        f'After {extracted_days} {check_day(extracted_days)} date will be {format_answer}!'
    )


@dp.message_handler(
    regexp=re.compile(
        '^(Яка дата|Який день) буде через [1-9]+[0-9]* (день|днів|дня),* якщо починати з '
        '([1-9]|0[1-9]|[1-2][0-9]|3[0-1]).([1-9]|0[1-9]|1[0-2]).([1-9]+.*[0-9]+)[?]*$|'
        '^What (date|day) will be after [1-9]+[0-9]* (day|days) if we start from '
        '([1-9]|0[1-9]|[1-2][0-9]|3[0-1]).([1-9]|0[1-9]|1[0-2]).([1-9]+.*[0-9]+)[?]*$',
        re.IGNORECASE
    )
)
async def find_date_after_days(message: types.Message):
    user_input = message.text
    extracted_data = exctract_from_user_input_days_and_date(user_input)
    days_num = extracted_data[0]
    month_day = extracted_data[1][0]
    month = extracted_data[1][1]
    year = extracted_data[1][2]

    try:
        user_date = datetime(day=month_day, month=month, year=year)
        format_user_date = user_date.strftime('%d.%m.%Y')
        answer = user_date + timedelta(days=days_num)
        format_answer = answer.strftime('%d.%m.%Y')

        await message.reply(
            f'If start from {format_user_date} after '
            f'{days_num} {check_day(days_num)}, date will be {format_answer}!'
        )
    except ValueError:
        await message.reply(
            f'<b>Some data is entered incorrectly!!!</b>\n\n'
            f'I think the problem is the {month_day} (first number in your date) because '
            f'the month you entered does not contain such day of the month.',
            parse_mode='HTML'
        )


# @dp.message_handler(content_types=ContentType.VOICE)
# async def delete_voice_except_admins(message: types.Message):
#     await delete_non_admin_message(message)


# @dp.message_handler(content_types=ContentType.VIDEO_NOTE)
# async def delete_video_note_except_admins(message: types.Message):
#     await delete_non_admin_message(message)


@dp.message_handler(content_types=ContentType.ANY)
async def check_bot_usage(message: types.Message):
    chat_id = message.chat.id
    bot_id = message.bot.id
    user_id = message.from_id
    username = message.from_user.username
    full_name = message.from_user.full_name
    message_id = message.message_id

    if username is None:
        username = ' '

    if full_name is None:
        full_name = ' '

    store_users_data.connect_to_db(user_id, username, full_name, chat_id)
