import asyncio

from bot.bot_main.main_objects_initialization import bot

DELETE_TIMEOUT = 60


async def delete_messages(message, bot_message):
    user_message = message.message_id
    await asyncio.sleep(DELETE_TIMEOUT)
    await bot.delete_message(chat_id=message.chat.id, message_id=user_message)
    await bot.delete_message(chat_id=message.chat.id, message_id=bot_message.message_id)
