from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, InputFile

from bot.bot_main.bot_classes.PhotoInscription import PhotoInscription
from bot.bot_main.for_photo_creation.photo_size import get_data_from_txt
from bot.bot_main.for_photo_creation.validate_args_number import validate_args
from bot.bot_main.main_objects_initialization import dp, bot
from bot.other_functions.delete_with_delay import delete_messages


@dp.message_handler(commands=['photo'])
async def get_photo_config(message: types.Message):
    await PhotoInscription.user_incription_config.set()
    bot_message = await message.reply(
        'Send me an image with description where have to '
        'be a text which i will add to your image, text must be '
        'in the following format: <code>example//100//200//233//500//20</code>\n\n'
        '<b>example</b> - this is a text that will be added to image)\n'
        '<b>100</b> - X coordinate (only integer allowed)\n'
        '<b>200</b> - Y coordinate (only integer allowed\n'
        '<b>233</b> - image width (only integer allowed)\n'
        '<b>500</b> - image height (only integer allowed)\n'
        '<b>20</b> - font size (only integer allowed)',
        parse_mode='HTML'
    )

    await delete_messages(message, bot_message)

@dp.message_handler(state=PhotoInscription.user_incription_config, content_types=ContentType.PHOTO)
async def create_photo(message: types.Message, state: FSMContext):
    # await delete_messages(message, user_message, bot_message)

    photo = message.photo[-1]
    await photo.download(destination_file='imgs/test.jpg')

    description = message.caption

    if not description:
        await message.reply('Sorry, that photo doesn’t have a caption. Try again.')
    else:
        user_input_lst = description.split('//', 5)
        formatted_lst = [args.strip() for args in user_input_lst]

        create_photo_using_args = await validate_args(formatted_lst, message)

        if create_photo_using_args:
            result_photo = InputFile('imgs/result.jpg')
            txt_data = get_data_from_txt()
            print(txt_data)
            await bot.send_photo(
                message.chat.id,
                photo=result_photo, caption=f'{txt_data}', parse_mode='HTML'
            )

    await state.finish()
