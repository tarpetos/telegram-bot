import mysql.connector

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main import main_objects_initialization
from bot.bot_main.bot_classes.TaskScheduler import TaskScheduler
from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.task_scheduler import back_to_planner_keyboard
from bot.keyboards.task_scheduler.scheduler_keyboard import scheduler_keyboard
from bot.other_functions import check_for_comma_and_dot, check_for_id_in_table
from bot.other_functions.close_keyboard import close_keyboard
from bot.other_functions.message_delete_exception import message_delete_control


@dp.message_handler(state='*', commands=['taskscheduler'])
async def scheduler_call(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_id
    username = message.from_user.username
    full_name = message.from_user.full_name
    main_objects_initialization.store_users_data.connect_to_db(user_id, username, full_name, chat_id)

    await message.reply('Choose a task scheduler function:', reply_markup=scheduler_keyboard)


@dp.callback_query_handler(text=['select'])
async def option_select(call: types.CallbackQuery):
    select_result = main_objects_initialization.unique_table.select_table('table_' + str(call.from_user.id))
    if not select_result:
        await call.message.edit_text('Table has no records', reply_markup=back_to_planner_keyboard.return_keyboard)
    else:
        all_tasks = ''.join(
            f'ID{task[0]} | Task №{task_number} | {task[1]}\n'
            for task_number, task in enumerate(select_result, 1)
        )

        await call.message.edit_text(all_tasks, reply_markup=back_to_planner_keyboard.return_keyboard)


@dp.callback_query_handler(text=['insert'])
async def option_insert(call: types.CallbackQuery):
    await TaskScheduler.insert.set()
    await call.answer('Enter the task text...', True)
    await call.message.delete()

@dp.message_handler(state=TaskScheduler.insert)
async def process_insert(message: types.Message, state: FSMContext):
    try:
        if len(message.text) > 768:
            raise ValueError

        main_objects_initialization.unique_table.insert_into_table(('table_' + str(message.from_user.id)), message.text)
        await message.answer('Data added successfully!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('Too many characters entered!', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['update'])
async def option_update(call: types.CallbackQuery):
    await TaskScheduler.update.set()
    await call.answer('Enter information in the format: "ID value", "task text"', True)
    await call.message.delete()


@dp.message_handler(state=TaskScheduler.update)
async def process_update(message: types.Message, state: FSMContext):
    try:
        user_data = check_for_comma_and_dot.check_user_data(message.text)
        user_id = check_for_comma_and_dot.check_user_id(message.text)

        if int(user_id) not in check_for_id_in_table.check_for_id(message):
            raise ValueError

        main_objects_initialization.unique_table.update_table(f'table_{message.from_user.id}', user_data, int(user_id))
        await message.answer('Data has been changed!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('Data is entered incorrectly!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except mysql.connector.errors.IntegrityError:
        await message.answer('You have already added this task', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['delete'])
async def option_delete(call: types.CallbackQuery):
    await TaskScheduler.delete.set()
    await call.answer('Enter the ID of the task you want to delete...', True)
    await call.message.delete()


@dp.message_handler(state=TaskScheduler.delete)
async def process_delete(message: types.Message, state: FSMContext):
    try:
        if int(message.text) not in check_for_id_in_table.check_for_id(message):
            raise ValueError

        main_objects_initialization.unique_table.delete_from_table(('table_' + str(message.from_user.id)), message.text)
        await message.answer('Data deleted successfully!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('Task ID was entered incorrectly!', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message_delete_control(message)

    await state.finish()


@dp.callback_query_handler(text=['back_to_scheduler'])
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        'Choose a task scheduler function:', reply_markup=scheduler_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['close_scheduler'])
async def close_scheduler(call: types.CallbackQuery):
    await close_keyboard(call)
