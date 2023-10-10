import asyncio
import re
from datetime import datetime, timedelta

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import IsReplyFilter
from aiogram.types import ContentType, InputFile

from bot.bot_main.for_photo_creation.remake_user_photo import (
    create_new_photo_auto_config,
)
from bot.config import (
    dp,
    bot,
    unique_table,
)
from bot.other_functions import currency_cost as cc
from bot.other_functions.check_date_words import check_day
from bot.other_functions.check_document_extension import (
    file_option_selector,
    parse_args,
    get_conversion_path_name,
)
from bot.other_functions.file_size_contoller import send_documents
from bot.other_functions.get_days_and_date_num import (
    extract_from_user_input_days_and_date,
    extract_from_user_input_days_num,
)
from bot.other_functions.image_to_file_converter import (
    ImageLoader,
    PDFConverter,
    DOCXConverter,
)
from bot.other_functions.morse_options import get_result
from bot.other_functions.remove_start_keyword import (
    remove_mem_from_start,
    remove_rand_mem_from_start,
)

# from bot.other_functions.image_to_file_converter import ImageQualityReducer

# reducer = ImageQualityReducer("test.jpg")
# reducer.reduce(100, "jpg")



# @dp.message_handler(IsReplyFilter(True), regexp="^audio$|^аудіо$", content_types=ContentType.AUDIO)
# async def process_audio(message: types.Message):
#     print(message.audio)
#     if message.reply_to_message.audio:
#         print(message.reply_to_message.audio)
#     else:
#         print("BEBRA")


@dp.message_handler(regexp="^morsec|^морзек")
async def morse_encryptor(message: types.Message):
    main_regex_len = 6
    user_input = message.text

    if len(user_input) == main_regex_len:
        return

    fixed_input = user_input[main_regex_len:].strip()
    result = get_result(fixed_input)
    await message.reply(text=result, parse_mode="HTML")


@dp.message_handler(regexp="^dtr delete tasks$|^дтр видали завдання$")
async def tasks_delete(message: types.Message):
    user_id = message.from_id
    unique_table.drop_remake_task_table(user_id)
    await message.reply(text="All tasks successfully deleted!!!")


@dp.message_handler(regexp="^dtr delete passwords$|^дтр видали паролі$")
async def passwords_delete(message: types.Message):
    user_id = message.from_id
    unique_table.drop_remake_password_table(user_id)
    await message.reply(text="All passwords successfully deleted!!!")


@dp.message_handler(regexp="^location$|^місцезнаходження$")
async def bot_location(message: types.Message):
    await bot.send_location(message.chat.id, latitude=49.924394, longitude=27.746868)


@dp.message_handler(regexp="^bitcoin$|^біткоін$|^біток$")
async def bitcoin_price(message: types.Message):
    await message.reply(
        f'<b>Bitcoin price right now:</b> <span class="tg-spoiler">{cc.bitcoin_price():.2f} $</span>\n',
        parse_mode="HTML",
    )


# @dp.message_handler(regexp="^dtr sticker$|^дтр стікер$")
# async def handle_message(message: types.Message):
#     await UserSticker.user_sticker.set()
#     await message.reply(
#         "Send me a sticker and I will save it to database."
#         "Then you can use stickers by typing command /sticker."
#     )


@dp.message_handler(regexp="^dtr example$|^дтр приклад$")
async def help_with_photo(message: types.Message):
    await message.reply(
        "<b><i>Below you can see examples how to use command</i></b> /photo\n\n"
        '<code>example</code> - only one argument. Text "example" '
        "will be printed in the top left corner, font size = 20.\n\n"
        '<code>example//40</code> - two arguments. Text "example" '
        "will be printed in the top left corner, font size = 40.\n\n"
        "<code>100//200</code> - two arguments.  Resize photo: width = 100, height = 200\n\n"
        '<code>example//100//200</code> - three arguments. Text "example" '
        "will be printed in position where coordinate X = 100 "
        "and coordinate Y = 200, font size = 20.\n\n"
        '<code>example//100//200//40</code> - four arguments. Text "example" '
        "will be printed in position where coordinate X = 100 "
        "and coordinate Y = 200, font size = 40.\n\n"
        '<code>example//100//200//1000//2000//50</code> - six arguments. Text "example" '
        "will be printed in position where coordinate X = 100 "
        "and coordinate Y = 200. New width will be equal to 1000 and height - 2000, font size = 50.\n",
        parse_mode="HTML",
    )


# @dp.message_handler(state=UserSticker.user_sticker, content_types=ContentType.STICKER)
# async def create_photo(message: types.Message, state: FSMContext):
#     sended_user_sticker = message.sticker.file_id
#     sticker_table.insert_into_sticker_table(sended_user_sticker)
#     await message.reply(f"Your sticker was added successfully!")
#     await state.finish()


@dp.message_handler(regexp="^random mem|^рандом мем", content_types=ContentType.PHOTO)
async def send_auto_config_photo_with_rand_text_clr(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file="imgs/test_auto_conf.jpg")
    get_user_photo_caption = message.caption
    formatted_text = remove_rand_mem_from_start(get_user_photo_caption)

    create_new_photo_auto_config(False, formatted_text)

    result_photo = InputFile("imgs/result_auto_conf.jpg")
    await bot.send_photo(message.chat.id, photo=result_photo)


@dp.message_handler(regexp="^mem|^мем", content_types=ContentType.PHOTO)
async def send_auto_config_photo_with_text(message: types.Message):
    photo = message.photo[-1]
    await photo.download(destination_file="imgs/test_auto_conf.jpg")
    get_user_photo_caption = message.caption
    formatted_text = remove_mem_from_start(get_user_photo_caption)

    create_new_photo_auto_config(True, formatted_text)

    result_photo = InputFile("imgs/result_auto_conf.jpg")
    await bot.send_photo(message.chat.id, photo=result_photo)


@dp.message_handler(
    IsReplyFilter(True),
    regexp=re.compile(
        "^reduce\\s*([1-9][0-9]?|100)?$|^знизити\\s*([1-9][0-9]?|100)?$", re.IGNORECASE
    ),
)
async def reduce_image(message: types.Message):
    replied_message = message.reply_to_message.content_type
    allowed_content = (ContentType.PHOTO, ContentType.DOCUMENT)

    if replied_message not in allowed_content:
        return None

    print(message.reply_to_message)


@dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT])
async def image_pdf_converter_filter(message: types.Message, state: FSMContext):
    first_photo = file_option_selector(message)
    if not first_photo:
        return

    await state.update_data(
        photo_0=first_photo,
        photo_counter=0,
        allowed_message_id_list=[message.message_id],
    )
    await state.set_state("image_state")


@dp.message_handler(
    content_types=[ContentType.PHOTO, ContentType.DOCUMENT], state="image_state"
)
async def image_pdf_converter_helper(message: types.Message, state: FSMContext):
    photo = file_option_selector(message)
    print(photo)
    if not photo:
        await state.finish()
        return

    async with state.proxy() as data:
        data["photo_counter"] += 1
        photo_counter = data["photo_counter"]
        data[f"photo_{photo_counter}"] = photo
        data[f"allowed_message_id_list"].append(message.message_id)

    if data["photo_counter"] > 20:
        await state.finish()


@dp.message_handler(
    IsReplyFilter(True),
    regexp=re.compile(
        "^pdf\\s*([1-9][0-9]?|100)?$|^пдф\\s*([1-9][0-9]?|100)?$", re.IGNORECASE
    ),
    state="image_state",
)
async def image_pdf_converter_end_state_handler(
        message: types.Message, state: FSMContext
):
    state_data = await state.get_data()
    user_message_ids = state_data["allowed_message_id_list"]
    check_message_id = message.reply_to_message.message_id
    replied_message = message.reply_to_message.content_type
    allowed_content = (ContentType.PHOTO, ContentType.DOCUMENT)

    if replied_message in allowed_content and check_message_id in user_message_ids:
        images_server_ids = [
            state_data[key]["file_id"]
            for key in state_data
            if key.startswith("photo") and not isinstance(state_data[key], int)
        ]
        file_loader = ImageLoader(message, "images")
        image_path_list = await file_loader.save_files(images_server_ids)

        bot_message = await message.reply("PDF and DOCX conversion started...")

        compression_level = parse_args(message, "pdf")
        print(compression_level)
        user_id = message.from_user.id
        conversion_pdf_path = get_conversion_path_name(
            "images", user_id, "pdf", filename="result"
        )
        pdf_converter = PDFConverter()
        pdf_converter.convert(
            conversion_pdf_path, image_path_list, compression_level=compression_level
        )

        conversion_docx_path = get_conversion_path_name(
            "images", user_id, "docx", filename="result"
        )
        docx_converter = DOCXConverter()
        docx_converter.convert(
            conversion_docx_path, image_path_list, compression_level=compression_level
        )

        bot_message_data = await send_documents(
            message, conversion_pdf_path, conversion_docx_path
        )
        await bot_message.edit_text(text=bot_message_data)

        file_loader.remove_temp_dir()
        await state.finish()


@dp.message_handler(state="*", regexp="^clear states$|^очистити стани$")
async def clear_states(message: types.Message, state: FSMContext):
    bot_message = await message.reply("Clearing states...")
    await asyncio.sleep(0.5)
    await state.finish()
    await bot.edit_message_text(
        "States are cleared.",
        chat_id=message.chat.id,
        message_id=bot_message.message_id,
    )


@dp.message_handler(IsReplyFilter(True), regexp="^msgd$|пвдв$")
async def delete_two_messages(message: types.Message):
    if message.reply_to_message.from_user.id == bot.id:
        replied_msg_id = message.reply_to_message.message_id
        await bot.delete_message(chat_id=message.chat.id, message_id=replied_msg_id)
        await message.delete()


@dp.message_handler(
    regexp=re.compile(
        "^(Яка дата|Який день) буде через [1-9]+[0-9]* (день|днів|дня)[?]*$|"
        "^What (date|day) will be after [1-9]+[0-9]* (day|days)[?]*$",
        re.IGNORECASE,
    )
)
async def find_date_after_days_from_current_date(message: types.Message):
    user_input = message.text
    extracted_days = extract_from_user_input_days_num(user_input)

    today = datetime.now()
    answer = today + timedelta(days=extracted_days)
    format_answer = answer.strftime("%d.%m.%Y")

    await message.reply(
        f"After {extracted_days} {check_day(extracted_days)} date will be {format_answer}!"
    )


@dp.message_handler(
    regexp=re.compile(
        "^(Яка дата|Який день) був [1-9]+[0-9]* (день|днів|дня) тому[?]*$|"
        "^What (date|day) was (it)? [1-9]+[0-9]* (day|days) ago[?]*$",
        re.IGNORECASE,
    )
)
async def find_date_before_days_from_current_date(message: types.Message):
    user_input = message.text
    extracted_days = extract_from_user_input_days_num(user_input)

    today = datetime.now()
    answer = today - timedelta(days=extracted_days)
    format_answer = answer.strftime("%d.%m.%Y")

    await message.reply(
        f"{extracted_days} {check_day(extracted_days)} ago it was {format_answer}!"
    )


@dp.message_handler(
    regexp=re.compile(
        "^(Яка дата|Який день) буде через [1-9]+[0-9]* (день|днів|дня),* якщо починати з "
        "([1-9]|0[1-9]|[1-2][0-9]|3[0-1]).([1-9]|0[1-9]|1[0-2]).([1-9]+.*[0-9]+)[?]*$|"
        "^What (date|day) will be after [1-9]+[0-9]* (day|days) if we start from "
        "([1-9]|0[1-9]|[1-2][0-9]|3[0-1]).([1-9]|0[1-9]|1[0-2]).([1-9]+.*[0-9]+)[?]*$",
        re.IGNORECASE,
    )
)
async def find_date_after_days(message: types.Message):
    user_input = message.text
    extracted_data = extract_from_user_input_days_and_date(user_input)
    days_num = extracted_data[0]
    month_day = extracted_data[1][0]
    month = extracted_data[1][1]
    year = extracted_data[1][2]

    try:
        user_date = datetime(day=month_day, month=month, year=year)
        format_user_date = user_date.strftime("%d.%m.%Y")
        answer = user_date + timedelta(days=days_num)
        format_answer = answer.strftime("%d.%m.%Y")

        await message.reply(
            f"If start from {format_user_date} after "
            f"{days_num} {check_day(days_num)}, date will be {format_answer}!"
        )
    except ValueError:
        await message.reply(
            f"<b>Some data is entered incorrectly!!!</b>\n\n"
            f"I think the problem is the {month_day} (first number in your date) because "
            f"the month you entered does not contain such day of the month.",
            parse_mode="HTML",
        )
