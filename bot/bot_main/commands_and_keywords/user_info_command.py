# import asyncio
#
# from aiogram import types
#
# from bot.bot_main.for_password_generation.generate_password import generate_token
# from bot.bot_main.main_objects_initialization import (
#     dp,
#     store_users_data,
#     token_table,
#     bot,
#     unique_table,
# )
# from bot.keyboards.token.token_keyboard import token_keyboard
# from bot.other_functions.close_keyboard import close_keyboard
# from bot.other_functions.encryption_decryption import encrypt, decrypt
#
# DELETE_TIMEOUT = 30
#
#
# @dp.message_handler(state="*", commands=["token"])
# async def user_data(message: types.Message):
#     get_username = message.from_user.username
#     user_id = message.from_user.id
#     full_name = message.from_user.full_name
#     chat_id = message.chat.id
#
#     if chat_id == user_id:
#         if unique_table.check_tables_to_allow_token(user_id):
#             store_users_data.connect_to_db(user_id, get_username, full_name, chat_id)
#
#             all_tokens = token_table.select_all_tokens()
#             user_token = token_table.select_token(user_id)
#
#             get_username = check_for_username(get_username)
#
#             if user_token in all_tokens:
#                 await message.reply(
#                     f"Username: {get_username}\n"
#                     f"Telegram ID: <code>{user_id}</code>\n\n"
#                     f"Desktop application token:\n<code>{decrypt(user_token)}</code>",
#                     parse_mode="HTML",
#                     reply_markup=token_keyboard,
#                 )
#             else:
#                 await message.reply(
#                     f"Username: {get_username}\n"
#                     f"Telegram ID: <code>{user_id}</code>\n\n",
#                     parse_mode="HTML",
#                     reply_markup=token_keyboard,
#                 )
#         else:
#             bot_message = await message.reply(
#                 "First, you need to use the password generator (/password) "
#                 "and create at least one password or click one of the buttons:\n"
#                 '"Show all passwords", "Change description", "Change password", "Delete password"!\n'
#                 "Only then can you use this command."
#             )
#             await asyncio.sleep(DELETE_TIMEOUT)
#             await bot.delete_message(chat_id=chat_id, message_id=bot_message.message_id)
#     else:
#         bot_message = await message.reply(
#             "This command can be used only in private conversation with bot!"
#         )
#         await asyncio.sleep(DELETE_TIMEOUT)
#         await bot.delete_message(chat_id=chat_id, message_id=bot_message.message_id)
#
#
# @dp.callback_query_handler(text="add_token")
# async def add_token(call: types.CallbackQuery):
#     random_token = generate_token()
#     user_token = encrypt(random_token)
#     get_username = call.from_user.username
#     user_id = call.from_user.id
#     token_table.add_token(user_id, user_token)
#
#     get_username = check_for_username(get_username)
#
#     await call.message.edit_text(
#         f"Username: {get_username}\n"
#         f"Telegram ID: <code>{user_id}</code>\n\n"
#         f"Desktop application token:\n<code>{random_token}</code>",
#         parse_mode="HTML",
#     )
#
#     await call.message.edit_reply_markup(reply_markup=token_keyboard)
#     await call.answer()
#
#
# @dp.callback_query_handler(text="delete_token")
# async def delete_token(call: types.CallbackQuery):
#     get_username = call.from_user.username
#     user_id = call.from_user.id
#
#     all_tokens = token_table.select_all_tokens()
#     user_token = token_table.select_token(user_id)
#
#     if user_token in all_tokens:
#         token_table.remove_token(user_id)
#     else:
#         await call.answer()
#         return
#
#     get_username = check_for_username(get_username)
#
#     await call.message.edit_text(
#         f"Username: {get_username}\n" f"Telegram ID: <code>{user_id}</code>",
#         parse_mode="HTML",
#     )
#
#     await call.message.edit_reply_markup(reply_markup=token_keyboard)
#     await call.answer()
#
#
# @dp.callback_query_handler(text="close_token")
# async def close_token(call: types.CallbackQuery):
#     await close_keyboard(call)
#
#
# def check_for_username(username):
#     if username is not None:
#         username = f"<code>{username}</code>"
#     else:
#         username = f'<span class="tg-spoiler"><b><i>You does not have a username🤷</i></b></span>'
#
#     return username
