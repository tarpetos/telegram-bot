from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

scheduler_keyboard = InlineKeyboardMarkup()

task_button1 = InlineKeyboardButton(text='View tasks', callback_data='select')
task_button2 = InlineKeyboardButton(text='Add task', callback_data='insert')
task_button3 = InlineKeyboardButton(text='Change task', callback_data='update')
task_button4 = InlineKeyboardButton(text='Delete task', callback_data='delete')
close_scheduler = InlineKeyboardButton(text='Close keyboard', callback_data='close_scheduler')

scheduler_keyboard.add(task_button1).add(task_button2).insert(task_button3).add(task_button4).add(close_scheduler)
