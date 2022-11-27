from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main import main_objects_initialization
from bot.bot_main.bot_classes.TaskScheduler import TaskScheduler
from bot.bot_main.main_objects_initialization import dp
from bot.keyboards import back_to_planner_keyboard
from bot.keyboards.scheduler_keyboard import scheduler_keyboard
from bot.other_functions import check_for_comma_and_dot, check_for_id_in_table


@dp.message_handler(commands=['taskscheduler'])
async def scheduler_call(message: types.Message):
    await message.reply('Виберіть функцію планувальника завдань:', reply_markup=scheduler_keyboard)


@dp.callback_query_handler(text=['select'])
async def option_select(call: types.CallbackQuery):
    select_result = main_objects_initialization.table.select_table('table_' + str(call.from_user.id))
    print(select_result)
    if not select_result:
        await call.message.edit_text('Таблиця не має записів', reply_markup=back_to_planner_keyboard.return_keyboard)
    else:
        all_tasks = ''.join(
            f'ID{task[0]} | завдання №{task_number + 1} | {task[1]}\n'
            for task_number, task in enumerate(select_result)
        )

        await call.message.edit_text(all_tasks, reply_markup=back_to_planner_keyboard.return_keyboard)


@dp.callback_query_handler(text=['insert'])
async def option_insert(call: types.CallbackQuery):
    await TaskScheduler.insert.set()
    await call.answer('Введіть текст завдання...', True)
    await call.message.delete()


@dp.message_handler(state=TaskScheduler.insert)
async def process_insert(message: types.Message, state: FSMContext):
    try:
        if len(message.text) > 768:
            raise ValueError

        main_objects_initialization.table.insert_into_table(('table_' + str(message.from_user.id)), message.text)
        await message.answer('Дані додано!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('Введено занадто багато символів!', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message.delete()
    await state.finish()


@dp.callback_query_handler(text=['update'])
async def option_update(call: types.CallbackQuery):
    await TaskScheduler.update.set()
    await call.answer('Введіть інформацію у форматі: значення ID, текст завдання', True)
    await call.message.delete()


@dp.message_handler(state=TaskScheduler.update)
async def process_update(message: types.Message, state: FSMContext):
    try:
        user_data = check_for_comma_and_dot.check_user_data(message.text)
        user_id = check_for_comma_and_dot.check_user_id(message.text)

        if int(user_id) not in check_for_id_in_table.check_for_id(message):
            raise ValueError

        main_objects_initialization.table.update_table(('table_' + str(message.from_user.id)), user_data, int(user_id))
        await message.answer('Дані змінено!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('Дані введено невірно!', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message.delete()
    await state.finish()


@dp.callback_query_handler(text=['delete'])
async def option_delete(call: types.CallbackQuery):
    await TaskScheduler.delete.set()
    await call.answer('Введіть ID завдання, яке хочете видалити...', True)
    await call.message.delete()


@dp.message_handler(state=TaskScheduler.delete)
async def process_delete(message: types.Message, state: FSMContext):
    try:
        if int(message.text) not in check_for_id_in_table.check_for_id(message):
            raise ValueError

        main_objects_initialization.table.delete_from_table(('table_' + str(message.from_user.id)), message.text)
        await message.answer('Дані видалено!', reply_markup=back_to_planner_keyboard.return_keyboard)
    except ValueError:
        await message.answer('ID завдання введено невірно!', reply_markup=back_to_planner_keyboard.return_keyboard)

    await message.delete()
    await state.finish()


@dp.callback_query_handler(text=['back_to_scheduler'])
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        'Виберіть функцію планувальника завдань:', reply_markup=scheduler_keyboard
    )
    await call.answer()
