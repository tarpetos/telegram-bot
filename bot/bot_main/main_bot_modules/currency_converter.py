from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main.bot_classes.ConverterForm import ConverterForm
from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.converter_keyboard import converter_keyboard
from bot.keyboards.currency_keyboard import currency_keyboard
from bot.keyboards.return_keyboard import return_keyboard
from bot.other_functions import currency_cost as cc
from bot.other_functions.close_keyboard import close_keyboard


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    await message.reply('Choose menu option💵:', reply_markup=currency_keyboard)


@dp.callback_query_handler(text=['currency_rate'])
async def exchange_rate(call: types.CallbackQuery):
    await call.message.edit_text(
        f'<b><i>BUY / SALE</i></b>\n'
        f'<code>'
        f'1 UAH = {cc.find_dollars_buy_in_hryvnias():.4f} / {cc.find_dollars_sale_in_hryvnias():.4f} USD\n'
        f'1 UAH = {cc.find_euros_buy_in_hryvnias():.4f} / {cc.find_euros_sale_in_hryvnias():.4f} EUR\n'
        f'1 EUR = {cc.find_dollars_buy_in_euros():.4f} / {cc.find_dollars_sale_in_euros():.4f} USD\n'
        f'1 EUR = {cc.find_hryvnias_buy_in_euros():.4f} / {cc.find_hryvnias_sale_in_euros():.4f} UAH\n'
        f'1 USD = {cc.find_euros_buy_in_dollars():.4f} / {cc.find_euros_sale_in_dollars():.4f} EUR\n'
        f'1 USD = {cc.find_hryvnias_buy_in_dollars():.4f} / {cc.find_hryvnias_sale_in_dollars():.4f} UAH'
        f'</code>', parse_mode='HTML', reply_markup=return_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['currency_converter'])
async def converter(call: types.CallbackQuery):
    await call.message.edit_text('Currency converter:', reply_markup=converter_keyboard)
    await call.answer()


@dp.callback_query_handler(text=['convert_dollar'])
async def convert_dollar(call: types.CallbackQuery):
    await ConverterForm.dollar.set()
    await call.answer('Enter the amount of $ to convert into euros and hryvnias...', True)


@dp.message_handler(state=ConverterForm.dollar)
async def process_dollar(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)

        await message.reply(
            f'Cost of buying dollars in hryvnias: '
            f'{answer / cc.find_dollars_buy_in_hryvnias():.4f}\n'
            f'Selling price of dollars in hryvnias: '
            f'{answer / cc.find_dollars_sale_in_hryvnias():.4f}\n'
            f'Cost of buying dollars in euros: '
            f'{answer / cc.find_dollars_buy_in_euros():.4f}\n'
            f'Selling price of dollars in euros: '
            f'{answer / cc.find_dollars_sale_in_euros():.4f}\n',
        )
    except ValueError:
        await message.reply('Invalid input. Must be a number. Try again.')

    await state.finish()


@dp.callback_query_handler(text=['convert_euro'])
async def convert_euro(call: types.CallbackQuery):
    await ConverterForm.euro.set()
    await call.answer('Enter the amount of € to convert to dollars and hryvnias...', True)


@dp.message_handler(state=ConverterForm.euro)
async def process_euro(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(
            f'Cost of buying euros in hryvnias: '
            f'{answer / cc.find_euros_buy_in_hryvnias():.4f}\n'
            f'Selling price of euros in hryvnias: '
            f'{answer / cc.find_euros_sale_in_hryvnias():.4f}\n'
            f'Cost of buying euros in dollars: '
            f'{answer / cc.find_euros_buy_in_dollars():.4f}\n'
            f'Selling price of euros in dollars: '
            f'{answer / cc.find_euros_sale_in_dollars():.4f}\n',
        )
    except ValueError:
        await message.reply('Invalid input. Must be a number. Try again.')

    await state.finish()


@dp.callback_query_handler(text=['convert_hryvnia'])
async def convert_hryvnia(call: types.CallbackQuery):
    await ConverterForm.hryvnia.set()
    await call.answer('Enter the amount of ₴ to convert to dollars and euros...', True)


@dp.message_handler(state=ConverterForm.hryvnia)
async def process_hryvnia(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(
            f'Cost of buying hryvnias in dollars:'
            f'{answer / cc.find_hryvnias_buy_in_dollars():.4f}\n'
            f'Selling price of hryvnias in dollars: '
            f'{answer / cc.find_hryvnias_sale_in_dollars():.4f}\n'
            f'Cost of buying hryvnias in euros: '
            f'{answer / cc.find_hryvnias_buy_in_euros():.4f}\n'
            f'Selling price of hryvnias in euros: '
            f'{answer / cc.find_hryvnias_sale_in_euros():.4f}\n',
        )
    except ValueError:
        await message.reply('Invalid input. Must be a number. Try again.')

    await state.finish()


@dp.callback_query_handler(text=['back_to_menu'])
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text('Choose menu option💵:', reply_markup=currency_keyboard)
    await call.answer()


@dp.callback_query_handler(text=['close_converter'])
async def close_converter(call: types.CallbackQuery):
    await close_keyboard(call)
