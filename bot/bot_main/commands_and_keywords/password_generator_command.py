import asyncio

import aiogram.utils.exceptions
import mysql.connector
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.bot_main.bot_classes.DuplicateDescriptionError import DuplicateDescriptionError
from bot.bot_main.bot_classes.PasswordGeneratorStates import PasswordGeneratorStates
from bot.bot_main.for_password_generation.generate_password import main_generation
# from bot.bot_main.for_password_generation import password_content_callbacks
# from bot.bot_main.for_password_generation import password_length_callbacks
from bot.bot_main.for_password_generation.password_content_callbacks import default_content_keyboard
from bot.bot_main.for_password_generation.password_length_callbacks import default_length_keyboard
from bot.bot_main.main_objects_initialization import dp, bot, unique_table, store_users_data
from bot.keyboards.password_generator.back_keyboard import back_to_telegram_generator_keyboard
from bot.keyboards.password_generator.download_app_keyboard import download_app_keyboard
from bot.keyboards.password_generator.generation_keyboard import third_generator_keyboard
from bot.keyboards.password_generator.radio_keyboard import first_generator_keyboard
from bot.keyboards.password_generator.set_length_keyboard import second_generator_keyboard
from bot.keyboards.password_generator.main_keyboard import password_start_keyboard
from bot.keyboards.password_generator.return_to_update_keyboard import password_generator_return_to_update
from bot.keyboards.password_generator.telegram_keyboard import password_telegram_keyboard
from bot.keyboards.password_generator.update_keyboard import password_generator_update_keyboard
from bot.other_functions import check_for_comma_and_dot, check_for_id_in_table
from bot.other_functions.check_for_repetetive_characters import check_if_repeatable_characters_is_present
from bot.other_functions.check_length_keyboard import keyboard_length_choice
from bot.other_functions.check_radio_keyboard import keyboard_content_choice
from bot.other_functions.close_keyboard import close_keyboard
from bot.other_functions.encryption_decryption import encrypt, decrypt
from bot.other_functions.work_with_json import send_json, remove_json
from bot.other_functions.message_delete_exception import message_delete_control

DELETE_TIMEOUT = 60

@dp.message_handler(state='*', commands=['password'])
async def password(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_id
    username = message.from_user.username
    full_name = message.from_user.full_name
    store_users_data.connect_to_db(user_id, username, full_name, chat_id)

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
    select_result = unique_table.select_pass_gen_table(f'pass_gen_table_{call.from_user.id}')

    if not select_result:
        await call.message.edit_text('Table has no records', reply_markup=back_to_telegram_generator_keyboard)
    else:
        all_passwords = ''.join(
            f'Password №{password_number}\n'
            f'ID: {password_data[0]}\n'
            f'Description: <code>{password_data[1]}</code>\n'
            f'Password: <code>{decrypt(password_data[2])}</code>\n'
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

            await call.answer()
        except aiogram.utils.exceptions.BadRequest:
            await call.message.edit_text(
                text='<b><i>Your passwords data is too big. I will send you a JSON file.</i></b>',
                reply_markup=back_to_telegram_generator_keyboard,
                parse_mode='HTML'
            )

            sent_message = await send_json(call)

            await call.answer()

            await asyncio.sleep(DELETE_TIMEOUT)
            await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)


@dp.callback_query_handler(text=['create_password'])
async def create_password(call: CallbackQuery):
    message_text = '<b><i>Choose what your password can contain:</i></b>'

    await call.message.edit_text(text=message_text, parse_mode='HTML', reply_markup=first_generator_keyboard)
    await call.answer()


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


        unique_table.update_password_desc(
            f'pass_gen_table_{message.from_user.id}', user_data, int(user_chosen_id)
        )

        await message.answer('Data has been changed!', reply_markup=password_generator_return_to_update)
    except ValueError:
        await message.answer('Entered data was incorrect!', reply_markup=password_generator_return_to_update)
    except mysql.connector.errors.IntegrityError:
        await message.answer(
            'Password with such description already exists!', reply_markup=password_generator_return_to_update
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

        encryped_password = encrypt(user_data)
        unique_table.update_password(
            f'pass_gen_table_{message.from_user.id}',
            encryped_password,
            user_data_length,
            repetetive_characters_in_password,
            int(user_chosen_id)
        )

        await message.answer('Data has been changed!', reply_markup=password_generator_return_to_update)
    except ValueError:
        await message.answer('Entered data was incorrect!', reply_markup=password_generator_return_to_update)
    except mysql.connector.errors.IntegrityError:
        await message.answer(
            'Password with such description already exists!', reply_markup=password_generator_return_to_update
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

        unique_table.delete_from_password_table(f'pass_gen_table_{message.from_user.id}', message.text)
        await message.answer('Data deleted successfully!', reply_markup=back_to_telegram_generator_keyboard)
    except ValueError:
        await message.answer('Password ID was entered incorrectly!', reply_markup=back_to_telegram_generator_keyboard)

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['password_app'])
async def password_app(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>Choose your system: </i></b>', parse_mode='HTML', reply_markup=download_app_keyboard
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
        '<b><i>You can see your JSON file below.</i></b>',
        parse_mode='HTML', reply_markup=back_to_telegram_generator_keyboard
    )

    sent_message = await send_json(call)
    remove_json(call)

    await call.answer()

    await asyncio.sleep(DELETE_TIMEOUT)
    await bot.delete_message(call.message.chat.id, message_id=sent_message.message_id)


@dp.callback_query_handler(text=['generate_password'])
async def generate_password(call: types.CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    necessary_keys = ['bot_message_id', 'password_contains', 'password_length']
    print(data)
    user_alphabet = data.get('password_contains')
    user_length = data.get('password_length')

    if all(key in data for key in necessary_keys):
        alphabet = keyboard_content_choice(user_alphabet)
        password_length = keyboard_length_choice(user_length)
        generated_password = main_generation(alphabet, password_length)
        data.update({'generated_pasword': generated_password})

        await call.answer(cache_time=2)

        await call.message.edit_text(
            text=f'Your password:\n<code>{generated_password}</code>',
            parse_mode='HTML'
        )
        await call.message.edit_reply_markup(
            reply_markup=third_generator_keyboard
        )
        await storage.set_data(data)
    else:
        await call.answer(
            'You need to press one of the button what your password could '
            'contain and choose password difficulty first!', True
        )


@dp.callback_query_handler(text=['store_in_db'])
async def option_set_description(call: types.CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    necessary_keys = ['bot_message_id', 'password_contains', 'password_length', 'generated_pasword']
    print(data)

    if all(key in data for key in necessary_keys):
        await PasswordGeneratorStates.set_description.set()
        await call.answer('Enter description text...', True)
    else:
        await call.answer(
            'You need to press one of the button what your password could '
            'contain, choose password difficulty and generate password first!', True
        )


@dp.message_handler(state=PasswordGeneratorStates.set_description)
async def process_description(message: types.Message, state: FSMContext):
    user_desc = message.text
    storage = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    data = await storage.get_data()
    data.update({'description': f'{user_desc}'})
    await storage.set_data(data)
    message_id = data['bot_message_id']
    print(data)

    if 'generated_pasword' in data:
        try:
            if len(user_desc) > 384:
                raise ValueError

            table_name = f'pass_gen_table_{message.from_id}'
            user_description = data['description']
            user_password = data['generated_pasword']
            password_length = keyboard_length_choice(data['password_length'])
            has_repetetive = check_if_repeatable_characters_is_present(user_password)

            await message.delete()

            if user_description in unique_table.select_description(table_name):
                raise DuplicateDescriptionError('Duplicate description in user table.')
            else:
                encryped_password = encrypt(user_password)
                unique_table.insert_password_data(
                    table_name,
                    user_description,
                    encryped_password,
                    password_length,
                    has_repetetive
                )

            await message.from_user.bot.edit_message_text(
                text=f'<i><b>Password saved successfuly!!!</b></i>\n\n'
                     f'Your description:\n<code>{data["description"]}</code>\n'
                     f'Your password:\n<code>{data["generated_pasword"]}</code>',
                chat_id=message.chat.id,
                message_id=message_id,
                parse_mode='HTML'
            )
            await message.from_user.bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=message_id,
                reply_markup=third_generator_keyboard
            )
        except ValueError:
            await message.from_user.bot.edit_message_text(
                text='Invalid input!\nToo many characters entered.',
                chat_id=message.chat.id,
                message_id=message_id,
            )
            await message.from_user.bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=message_id,
                reply_markup=third_generator_keyboard
            )
        except DuplicateDescriptionError:
            await message.from_user.bot.edit_message_text(
                text='Invalid input!\nDescription already in the table!!!',
                chat_id=message.chat.id,
                message_id=message_id,
            )
            await message.from_user.bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=message_id,
                reply_markup=third_generator_keyboard
            )

    await state.finish()
    await storage.set_data(data)


@dp.callback_query_handler(text=['next_to_second'])
async def next_to_second(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    necessary_keys = ['bot_message_id', 'password_contains']
    print(data)

    if 'password_length' not in data:
        if all(key in data for key in necessary_keys):
            await call.message.edit_text(
                '<b><i>Choose the password difficulty:</i></b>\n\n',
                reply_markup=second_generator_keyboard,
                parse_mode='HTML'
            )
        else:
            await call.message.edit_text(text='<i><b>Choose what your password can contain:</b></i>', parse_mode='HTML')
            await call.message.edit_reply_markup(reply_markup=first_generator_keyboard)
            await call.answer('You should select any of these before continue!', True)
    else:
        await call.message.edit_text(
            '<b><i>Choose the password difficulty:</i></b>\n\n',
            parse_mode='HTML'
        )
        await call.message.edit_reply_markup(reply_markup=second_generator_keyboard)
        await call.answer()


@dp.callback_query_handler(text=['next_to_third'])
async def next_to_third(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    necessary_keys = ['bot_message_id', 'password_contains', 'password_length']
    print(data)

    if 'generated_pasword' in data:
        if data['description']:
            await call.message.edit_text(
                text = f'<i><b>Password saved successfuly!!!</b></i>\n\n'
                       f'Your description:\n<code>{data["description"]}</code>\n'
                       f'Your password:\n<code>{data["generated_pasword"]}</code>',
                reply_markup = third_generator_keyboard,
                parse_mode = 'HTML'
            )
        else:
            await call.message.edit_text(
                text=f'Your password:\n<code>{data["generated_pasword"]}</code>',
                reply_markup=third_generator_keyboard,
                parse_mode='HTML'
            )
    else:
        if all(key in data for key in necessary_keys):
            await call.message.edit_text(
                '<b><i>Generate your password and write it to the database! </i></b>\n\n',
                reply_markup=third_generator_keyboard,
                parse_mode='HTML'
            )
        else:
            await call.message.edit_text(text='<i><b>Choose the password difficulty:</b></i>', parse_mode='HTML')
            await call.message.edit_reply_markup(reply_markup=second_generator_keyboard)
            await call.answer('You need to choose what will contain your password and choose its difficulty!', True)


@dp.callback_query_handler(text=['main_generator_menu'])
async def main_generator_menu(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    await storage.finish()

    default_content_keyboard()
    default_length_keyboard()

    await call.message.edit_text(
        '<b><i>Choose menu option: </i></b>\n\n',
        reply_markup=password_telegram_keyboard,
        parse_mode='HTML'
    )


@dp.callback_query_handler(text=['back_to_first'])
async def back_to_first(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    print(data)

    message_text = '<b><i>Choose what your password can contain:</i></b>'

    await call.message.edit_text(text=message_text, parse_mode='HTML', reply_markup=first_generator_keyboard)
    await call.answer()


@dp.callback_query_handler(text=['back_to_second'])
async def back_to_second(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    user_choice = data.get('password_length')
    print(user_choice)

    message_text = '<b><i>Choose the password difficulty:</i></b>\n\n'

    await call.message.edit_text(text=message_text, parse_mode='HTML')
    await call.message.edit_reply_markup(reply_markup=second_generator_keyboard)
    await call.answer()


@dp.callback_query_handler(text=['return_to_update_menu'])
async def return_to_update_menu(call: CallbackQuery):
    await call.message.edit_text(
        '<b><i>What do you want to change?:</i></b>',
        parse_mode='HTML', reply_markup=password_generator_update_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['back_to_telegram_generator'])
async def back_to_telegram_generator(call: CallbackQuery):
    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    await storage.finish()

    default_content_keyboard()
    default_length_keyboard()

    await call.message.edit_text(
        '<b><i>Choose menu option: </i></b>',
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
