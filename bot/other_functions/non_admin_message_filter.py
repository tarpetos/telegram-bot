from bot.bot_main.main_objects_initialization import bot


def get_admin_ids(administrators_list) -> list:
    administrators_id_list = []

    for admin in range(len(administrators_list)):
        administrators_id_list.append(administrators_list[admin]['user']['id'])

    return administrators_id_list


async def delete_non_admin_message(message):
    if message.chat.type == 'supergroup':
        administrators_list = await bot.get_chat_administrators(message.chat.id)

        administrators_id_list = get_admin_ids(administrators_list)

        if message.from_id not in administrators_id_list:
            await message.delete()
