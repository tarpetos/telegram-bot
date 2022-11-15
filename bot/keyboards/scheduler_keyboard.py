from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

scheduler_keyboard = InlineKeyboardMarkup()

task_button1 = InlineKeyboardButton(text='Перегляд завдань', callback_data='select')
task_button2 = InlineKeyboardButton(text='Додати завдання', callback_data='insert')
task_button3 = InlineKeyboardButton(text='Змінити завдання', callback_data='update')
task_button4 = InlineKeyboardButton(text='Видалити завдання', callback_data='delete')

scheduler_keyboard.add(task_button1).add(task_button2).insert(task_button3).add(task_button4)
