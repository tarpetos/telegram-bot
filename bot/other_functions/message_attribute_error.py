import aiogram.utils.exceptions


async def message_attribute_control(call):
    try:
        await call.message.reply_to_message.delete()
    except AttributeError:
        pass
    except aiogram.utils.exceptions.MessageCantBeDeleted:
        pass
