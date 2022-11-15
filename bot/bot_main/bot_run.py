from aiogram import executor

from bot.bot_main import main_objects_initialization
from bot.bot_main.main_bot_modules import main_commands, random_numbers_generation, task_scheduler, show_user_info, \
    time_commands, sticker_command, weather_command, currency_converter, youtube_search_command, mention_all_command, \
    react_on_users_action, location_bitcoin, keywords_for_conversation_with_bot

bot = main_objects_initialization.bot
dp = main_objects_initialization.dp


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
