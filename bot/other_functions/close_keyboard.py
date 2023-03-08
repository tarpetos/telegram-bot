from bot.other_functions.message_attribute_error import message_attribute_control


async def close_keyboard(call):
    await message_attribute_control(call)
    await call.message.delete()
    await call.answer()
