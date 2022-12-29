from aiogram import types

from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.password_generator.set_length_keyboard import very_easy_button, easy_button, normal_button, \
    hard_button, very_hard_button, unbreakable_button, second_generator_keyboard
from bot.other_functions.change_state_mem_storage import update_with_length_state


def default_length_keyboard():
    very_easy_button.text = 'Very easy'
    easy_button.text = 'Easy'
    normal_button.text = 'Normal'
    hard_button.text = 'Hard'
    very_hard_button.text = 'Very hard'
    unbreakable_button.text = 'Unbreakable'


@dp.callback_query_handler(text=['very_easy'])
async def option_very_easy(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 10 characters!',
            True
        )

        if very_easy_button.text == 'Very easy ✅':
            pass
        else:
            very_easy_button.text = 'Very easy ✅'
            easy_button.text = 'Easy'
            normal_button.text = 'Normal'
            hard_button.text = 'Hard'
            very_hard_button.text = 'Very hard'
            unbreakable_button.text = 'Unbreakable'

            await call.message.edit_reply_markup(second_generator_keyboard)


@dp.callback_query_handler(text=['easy'])
async def option_easy(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 20 characters!',
            True
        )

        if easy_button.text == 'Easy ✅':
            pass
        else:
            very_easy_button.text = 'Very easy'
            easy_button.text = 'Easy ✅'
            normal_button.text = 'Normal'
            hard_button.text = 'Hard'
            very_hard_button.text = 'Very hard'
            unbreakable_button.text = 'Unbreakable'

            await call.message.edit_reply_markup(second_generator_keyboard)


@dp.callback_query_handler(text=['normal'])
async def option_normal(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 30 characters!',
            True
        )

        if normal_button.text == 'Normal ✅':
            pass
        else:
            very_easy_button.text = 'Very easy'
            easy_button.text = 'Easy'
            normal_button.text = 'Normal ✅'
            hard_button.text = 'Hard'
            very_hard_button.text = 'Very hard'
            unbreakable_button.text = 'Unbreakable'

            await call.message.edit_reply_markup(second_generator_keyboard)


@dp.callback_query_handler(text=['hard'])
async def option_hard(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 40 characters!',
            True
        )

        if hard_button.text == 'Hard ✅':
            pass
        else:
            very_easy_button.text = 'Very easy'
            easy_button.text = 'Easy'
            normal_button.text = 'Normal'
            hard_button.text = 'Hard ✅'
            very_hard_button.text = 'Very hard'
            unbreakable_button.text = 'Unbreakable'

            await call.message.edit_reply_markup(second_generator_keyboard)


@dp.callback_query_handler(text=['very_hard'])
async def option_very_hard(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 50 characters!',
            True
        )

        if very_hard_button.text == 'Very hard ✅':
            pass
        else:
            very_easy_button.text = 'Very easy'
            easy_button.text = 'Easy'
            normal_button.text = 'Normal'
            hard_button.text = 'Hard'
            very_hard_button.text = 'Very hard ✅'
            unbreakable_button.text = 'Unbreakable'

            await call.message.edit_reply_markup(second_generator_keyboard)


@dp.callback_query_handler(text=['unbreakable'])
async def option_unbreakable(call: types.CallbackQuery):
    result = await update_with_length_state(call)
    print(result)

    if result is None:
        pass
    else:
        await call.answer(
            'Length of your password will be equal to 100 characters!',
            True
        )

        if unbreakable_button.text == 'Unbreakable ✅':
            pass
        else:
            very_easy_button.text = 'Very easy'
            easy_button.text = 'Easy'
            normal_button.text = 'Normal'
            hard_button.text = 'Hard'
            very_hard_button.text = 'Very hard'
            unbreakable_button.text = 'Unbreakable ✅'

            await call.message.edit_reply_markup(second_generator_keyboard)
