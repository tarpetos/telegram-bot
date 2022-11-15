from aiogram import types

from bot.bot_main.main_objects_initialization import dp


@dp.message_handler(commands=['id'])
async def user_data(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('ID', callback_data='user_id')
    keyboard_markup.row(user_id_btn)

    if message.from_user.username is not None:
        message.from_user.username = f'<code>{message.from_user.username}</code>'
    else:
        message.from_user.username = f'<span class="tg-spoiler"><b><i>користувач не має імені🤷</i></b></span>'

    await message.answer(
        f'Ім’я користувача: {message.from_user.username}\n\n'
        'Натисни кнопку, щоб побачити свій ID...', parse_mode='HTML', reply_markup=keyboard_markup
    )

    await message.delete()


@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f'Ваш ID: {callback_query.from_user.id}', True)
