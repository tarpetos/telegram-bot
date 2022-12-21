from bot.bot_main.main_objects_initialization import dp


async def update_state(call):
    choice = call.data

    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()

    data.update({'bot_message_id': call.message.message_id})
    data.update({'password_contains': choice})

    await storage.set_data(data)
    data = await storage.get_data()

    return data


async def update_with_length_state(call):
    choice = call.data

    storage = dp.current_state(chat=call.message.chat.id, user=call.from_user.id)
    data = await storage.get_data()
    necessary_keys = ['bot_message_id', 'password_contains']

    if all(key in data for key in necessary_keys):
        data.update({'password_length': choice})

        await storage.set_data(data)
        data = await storage.get_data()

        return data
    else:
        await call.answer(
            'You should press one of the button what your password could contain '
            'first. And only then you can choose difficulty!', True, cache_time=2
        )
        return
