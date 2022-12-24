import aiogram.utils.exceptions


async def message_delete_control(message):
    try:
        await message.delete()
    except aiogram.utils.exceptions.MessageCantBeDeleted:
        pass
