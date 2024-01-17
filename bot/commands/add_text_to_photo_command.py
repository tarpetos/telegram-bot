from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InputFile

from .commands_utils.states import PhotoInscription
from .commands_utils.for_photo_creation.photo_size import get_data_from_txt
from .commands_utils.for_photo_creation.validate_args_number import validate_args
from ..config import dp, bot
from ..enums import Command
from bot.commands.commands_utils.delete_with_delay import delete_messages


@dp.message_handler(state="*", commands=Command.IMAGE_EDITOR)
async def get_photo_config(message: types.Message):
    await PhotoInscription.user_inscription_config.set()
    bot_message = await message.reply(
        "Send me an image with description where have to "
        "be a text which i will add to your image, text must be "
        "in the following format: <code>example//100//200//233//500//20</code>\n\n"
        "<b>example</b> - this is a text that will be added to image)\n"
        "<b>100</b> - X coordinate (only integer allowed)\n"
        "<b>200</b> - Y coordinate (only integer allowed\n"
        "<b>233</b> - image width (only integer allowed)\n"
        "<b>500</b> - image height (only integer allowed)\n"
        "<b>20</b> - font size (only integer allowed)",
        parse_mode="HTML",
    )

    await delete_messages(message, bot_message)


@dp.message_handler(
    state=PhotoInscription.user_inscription_config, content_types=ContentType.PHOTO
)
async def create_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    await photo.download(destination_file="imgs/test.jpg")

    description = message.caption

    if not description:
        await message.reply("Sorry, that photo doesn’t have a caption. Try again.")
    else:
        user_input_lst = description.split("//", 5)
        formatted_lst = [args.strip() for args in user_input_lst]

        create_photo_using_args = await validate_args(formatted_lst, message)

        if create_photo_using_args:
            result_photo = InputFile("imgs/result.jpg")
            txt_data = get_data_from_txt()
            await bot.send_photo(
                message.chat.id,
                photo=result_photo,
                caption=f"{txt_data}",
                parse_mode="HTML",
            )

    await state.finish()
