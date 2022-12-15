import asyncio

import aiogram.utils.exceptions
import mysql.connector
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.bot_main import main_objects_initialization
from bot.bot_main.bot_classes.PasswordGeneratorStates import PasswordGeneratorStates
from bot.bot_main.main_objects_initialization import dp, bot
from bot.keyboards.password_generator_back_keyboard import back_to_telegram_generator_keyboard
from bot.keyboards.password_generator_back_to_second import password_generator_back_to_second
from bot.keyboards.password_generator_download_app_keyboard import download_app_keyboard
from bot.keyboards.password_generator_generation_keyboard import third_generator_keyboard
from bot.keyboards.password_generator_main_create_menu_keyboard import second_generator_keyboard
from bot.keyboards.password_generator_main_keyboard import password_start_keyboard
from bot.keyboards.password_generator_radio_keyboard import first_generator_keyboard
from bot.keyboards.password_generator_return_to_update_keyboard import password_generator_return_to_update
from bot.keyboards.password_generator_telegram_keyboard import password_telegram_keyboard
from bot.keyboards.password_generator_update_keyboard import password_generator_update_keyboard
from bot.other_functions import check_for_comma_and_dot, check_for_id_in_table
from bot.other_functions.check_for_integer import check_password_length_input
from bot.other_functions.check_for_repetetive_characters import check_if_repeatable_characters_is_present
from bot.other_functions.close_keyboard import close_keyboard
from bot.other_functions.work_with_json import send_json, remove_json
from bot.other_functions.message_delete_exception import message_delete_control


DELETE_TIMEOUT = 60

@dp.message_handler(commands=['password'])
async def password(message: types.Message):
    await message.reply(
        '<b><i>Welcome to password generator</i></b> 🔒\n\n'
        '<code>'
        'As you can see below, there are two buttons. By clicking on the first button, '
        'you will go to the password generator embedded in me. After clicking the second button, '
        'you will be presented with options to download the application to your local machine.'
        '</code>',
        reply_markup=password_start_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['telegram_password'])
async def telegram_password(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Choose menu option:</i></b>\n\n',
        reply_markup=password_telegram_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['show_password'])
async def option_show_passwords(call: types.CallbackQuery):
    select_result = main_objects_initialization.unique_table.select_pass_gen_table(f'pass_gen_table_{call.from_user.id}')

    if not select_result:
        await call.message.edit_text('Table has no records', reply_markup=back_to_telegram_generator_keyboard)
    else:
        all_passwords = ''.join(
            f'Password №: {password_number}\n'
            f'ID: {password_data[0]}\n'
            f'Password description: <code>{password_data[1]}</code>\n'
            f'Password: <code>{password_data[2]}</code>\n'
            f'Length: {password_data[3]}\n'
            f'Has repetetive?: {password_data[4]}\n\n'
            for password_number, password_data in enumerate(select_result, 1)
        )

        try:
            await call.message.edit_text(
                text=all_passwords,
                reply_markup=back_to_telegram_generator_keyboard,
                parse_mode='HTML'
            )
        except aiogram.utils.exceptions.BadRequest:
            await call.message.edit_text(
                text='<b><i>Your passwords data is too big. I will send you a json file.</i></b>',
                reply_markup=back_to_telegram_generator_keyboard,
                parse_mode='HTML'
            )

            sent_message = await send_json(call)

            await call.answer()

            await asyncio.sleep(DELETE_TIMEOUT)
            await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)

    await call.answer()


@dp.callback_query_handler(text=['create_password'])
async def create_password(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Enter password description and password length (required):</i></b>\n\n',
        reply_markup=first_generator_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['change_desc_pass'])
async def change_desc_pass(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>What do you want to change?:</i></b>\n\n',
        reply_markup=password_generator_update_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['change_description'])
async def change_password(call: CallbackQuery):
    await PasswordGeneratorStates.update_description.set()
    await call.answer('Enter description information in the format: "ID value", "description text"', True)
    await call.message.delete()


@dp.message_handler(state=PasswordGeneratorStates.update_description)
async def process_description_update(message: types.Message, state: FSMContext):
    try:
        user_data = check_for_comma_and_dot.check_user_data(message.text)
        user_chosen_id = check_for_comma_and_dot.check_user_id(message.text)

        if int(user_chosen_id) not in check_for_id_in_table.check_for_password_id(message):
            raise ValueError


        main_objects_initialization.unique_table.update_password_desc(
            f'pass_gen_table_{message.from_user.id}', user_data, int(user_chosen_id)
        )

        await message.answer('Data has been changed!', reply_markup=password_generator_return_to_update)
    except ValueError:
        await message.answer('Entered data was incorrect!', reply_markup=password_generator_return_to_update)
    except mysql.connector.errors.IntegrityError:
        await message.answer(
            'Password with such description already exists', reply_markup=password_generator_return_to_update
        )

    await message_delete_control(message)

    await state.finish()

@dp.callback_query_handler(text=['change_password'])
async def change_password(call: CallbackQuery):
    await PasswordGeneratorStates.update_password.set()
    await call.answer('Enter password information in the format: "ID value", "password text"', True)
    await call.message.delete()


@dp.message_handler(state=PasswordGeneratorStates.update_password)
async def process_password_update(message: types.Message, state: FSMContext):
    try:
        user_data = check_for_comma_and_dot.check_user_data(message.text)
        user_data_length = len(user_data)
        repetetive_characters_in_password = check_if_repeatable_characters_is_present(user_data)
        user_chosen_id = check_for_comma_and_dot.check_user_id(message.text)

        if int(user_chosen_id) not in check_for_id_in_table.check_for_password_id(message):
            raise ValueError

        main_objects_initialization.unique_table.update_password(
            f'pass_gen_table_{message.from_user.id}',
            user_data,
            user_data_length,
            repetetive_characters_in_password,
            int(user_chosen_id)
        )

        await message.answer('Data has been changed!', reply_markup=password_generator_return_to_update)
    except ValueError:
        await message.answer('Entered data was incorrect!', reply_markup=password_generator_return_to_update)
    except mysql.connector.errors.IntegrityError:
        await message.answer(
            'Password with such description already exists', reply_markup=password_generator_return_to_update
        )

    await message_delete_control(message)

    await state.finish()

@dp.callback_query_handler(text=['delete_password'])
async def delete_password(call: CallbackQuery):
    await PasswordGeneratorStates.delete.set()
    await call.answer('Enter password ID and all data about that password will be removed.', True)
    await call.message.delete()


@dp.message_handler(state=PasswordGeneratorStates.delete)
async def process_password_update(message: types.Message, state: FSMContext):
    try:
        if int(message.text) not in check_for_id_in_table.check_for_password_id(message):
            raise ValueError

        main_objects_initialization.unique_table.delete_from_table(f'pass_gen_table_{message.from_user.id}', message.text)
        await message.answer('Data deleted successfully!', reply_markup=back_to_telegram_generator_keyboard)
    except ValueError:
        await message.answer('Password ID was entered incorrectly!', reply_markup=back_to_telegram_generator_keyboard)

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['password_app'])
async def password_app(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>Choose your system: </i></b>', parse_mode='HTML', reply_markup=download_app_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['windows_installer'])
async def windows_installer(call: CallbackQuery):
    with open('password_generator_app/Password_Generator_Windows_Setup.zip', 'rb') as zip_archive:
        zip_content = zip_archive.read()

    sent_message = await call.bot.send_document(
        chat_id=call.message.chat.id,
        document=('Password_Generator_Windows_Setup.zip', zip_content),
        caption='Password for archive: <code>123454321</code>',
        parse_mode = 'HTML'
    )

    await call.answer()

    await asyncio.sleep(DELETE_TIMEOUT)
    await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)


@dp.callback_query_handler(text=['linux_macos'])
async def linux_macos(call: CallbackQuery):
    with open('password_generator_app/Password_Generator_Linux_MacOS.zip', 'rb') as zip_archive:
        zip_content = zip_archive.read()

    sent_message = await call.bot.send_document(
        chat_id=call.message.chat.id,
        document=('Password_Generator_Linux_MacOS.zip', zip_content),
        caption='Password for archive: <code>123454321</code>',
        parse_mode='HTML'
    )

    await call.answer()

    await asyncio.sleep(DELETE_TIMEOUT)
    await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)


@dp.callback_query_handler(text=['json_password'])
async def json_password(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>You can see your json file below.</i></b>',
        parse_mode='HTML', reply_markup=back_to_telegram_generator_keyboard
    )

    sent_message = await send_json(call)
    remove_json(call)

    await call.answer()

    await asyncio.sleep(DELETE_TIMEOUT)
    await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)


@dp.callback_query_handler(text=['all_characters'])
async def option_all_characters(call: types.CallbackQuery):
    await call.answer('Now your password can contain all possible characters!', True)


@dp.callback_query_handler(text=['only_letters'])
async def option_only_letters(call: types.CallbackQuery):
    await call.answer('Now your password can contain only small and big english letters!', True)


@dp.callback_query_handler(text=['only_digits'])
async def option_only_digits(call: types.CallbackQuery):
    await call.answer('Now your password can contain only digits!', True)


@dp.callback_query_handler(text=['letters_digits'])
async def option_letters_digits(call: types.CallbackQuery):
    await call.answer('Now your password can contain english letters and digits!', True)


@dp.callback_query_handler(text=['letters_signs'])
async def option_letters_signs(call: types.CallbackQuery):
    await call.answer('Now your password can contain all letters and signs!', True)


@dp.callback_query_handler(text=['digits_signs'])
async def option_digits_signs(call: types.CallbackQuery):
    await call.answer('Now your password can contain digits and signs!', True)


@dp.callback_query_handler(text=['set_description'])
async def option_set_description(call: types.CallbackQuery):
    await PasswordGeneratorStates.set_description.set()
    await call.answer('Enter description text...', True)
    await call.message.delete()

@dp.message_handler(state=PasswordGeneratorStates.set_description)
async def process_description(message: types.Message, state: FSMContext):
    try:
        if len(message.text) > 384:
            raise ValueError

        # main_objects_initialization.unique_table.insert_into_table((f'pass_gen_table_{message.from_user.id}', message.text)
        await message.answer('Description saved!', reply_markup=password_generator_back_to_second)
    except ValueError:
        await message.answer(
            'Invalid input!\nToo many characters entered.', reply_markup=password_generator_back_to_second
        )

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['set_length'])
async def option_set_length(call: types.CallbackQuery):
    await PasswordGeneratorStates.set_length.set()
    await call.answer('Enter password length...', True)
    await call.message.delete()

@dp.message_handler(state=PasswordGeneratorStates.set_length)
async def process_length(message: types.Message, state: FSMContext):
    user_input = message.text

    try:
        if check_password_length_input(user_input):
            pass

        # main_objects_initialization.unique_table.insert_into_table((f'pass_gen_table_{message.from_user.id}', message.text)
        await message.answer('Password length saved!', reply_markup=password_generator_back_to_second)
    except ValueError:
        await message.answer(
            'Ivalid input!\nPassword length can contain only integers in range from 1 to 384.',
            reply_markup=password_generator_back_to_second
        )

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['next_to_second'])
async def next_to_second(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Choose what your password will contain: </i></b>\n\n',
        reply_markup=second_generator_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['next_to_third'])
async def next_to_third(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Generate your password and write it to database! </i></b>\n\n',
        reply_markup=third_generator_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['main_generator_menu'])
async def main_generator_menu(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Choose menu option: </i></b>\n\n',
        reply_markup=password_telegram_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['back_to_first'])
async def back_to_second(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>Choose what your password can contain:</i></b>',
        parse_mode='HTML', reply_markup=first_generator_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['back_to_second'])
async def back_to_first(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>Enter password description and password length (required):</i></b>',
        parse_mode='HTML', reply_markup=second_generator_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['return_to_update_menu'])
async def return_to_update_menu(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>What do you want to change?:</i></b>',
        parse_mode='HTML', reply_markup=password_generator_update_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['back_to_telegram_generator'])
async def back_to_telegram_generator(call: CallbackQuery):
    await call.message.edit_text(
        f'<b><i>Choose menu option: </i></b>',
        parse_mode='HTML', reply_markup=password_telegram_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['back_to_main_menu'])
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Welcome to password generator</i></b> 🔒\n\n'
        '<code>'
        'As you can see below, there are two buttons. By clicking on the first button, '
        'you will go to the password generator embedded in me. After clicking the second button, '
        'you will be presented with options to download the application to your local machine.'
        '</code>',
        parse_mode='HTML',
        reply_markup=password_start_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['close_app'])
async def close_app(call: CallbackQuery):
    await close_keyboard(call)
