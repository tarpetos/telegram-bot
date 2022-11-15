from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main.bot_classes.ConverterForm import ConverterForm
from bot.bot_main.main_objects_initialization import dp
from bot.keyboards.converter_keyboard import converter_keyboard
from bot.keyboards.currency_keyboard import currency_keyboard
from bot.keyboards.return_keyboard import return_keyboard
from bot.other_functions import currency_cost as cc


@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    await message.reply('Виберіть опцію меню💵:', reply_markup=currency_keyboard)


@dp.callback_query_handler(text=['currency_rate'])
async def exchange_rate(call: types.CallbackQuery):
    await call.message.edit_text(
        f'<b><i>КУПІВЛЯ / ПРОДАЖ</i></b>\n'
        f'<code>'
        f'1 гривня = {cc.find_dollars_buy_in_hryvnias():.4f} / {cc.find_dollars_sale_in_hryvnias():.4f} долара\n'
        f'1 гривня = {cc.find_euros_buy_in_hryvnias():.4f} / {cc.find_euros_sale_in_hryvnias():.4f} євро\n'
        f'1 євро   = {cc.find_dollars_buy_in_euros():.4f} / {cc.find_dollars_sale_in_euros():.4f} долара\n'
        f'1 євро   = {cc.find_hryvnias_buy_in_euros():.4f} / {cc.find_hryvnias_sale_in_euros():.4f} гривень\n'
        f'1 долар  = {cc.find_euros_buy_in_dollars():.4f} / {cc.find_euros_sale_in_dollars():.4f} євро\n'
        f'1 долар  = {cc.find_hryvnias_buy_in_dollars():.4f} / {cc.find_hryvnias_sale_in_dollars():.4f} гривень'
        f'</code>', parse_mode='HTML', reply_markup=return_keyboard
    )
    await call.answer()


@dp.callback_query_handler(text=['currency_converter'])
async def converter(call: types.CallbackQuery):
    await call.message.edit_text('Конвертер валют:', reply_markup=converter_keyboard)
    await call.answer()


@dp.callback_query_handler(text=['convert_dollar'])
async def convert_dollar(call: types.CallbackQuery):
    await ConverterForm.dollar.set()
    await call.answer('Введіть кількість $ для конвертування в євро та гривні...')


@dp.message_handler(state=ConverterForm.dollar)
async def process_dollar(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)

        await message.reply(
            f'Вартість покупки доларів в гривнях: '
            f'{answer / cc.find_dollars_buy_in_hryvnias():.4f}\n'
            f'Вартість продажі доларів в гривнях: '
            f'{answer / cc.find_dollars_sale_in_hryvnias():.4f}\n'
            f'Вартість покупки доларів в євро: '
            f'{answer / cc.find_dollars_buy_in_euros():.4f}\n'
            f'Вартість продажі доларів в євро: '
            f'{answer / cc.find_dollars_sale_in_euros():.4f}\n',
        )
    except ValueError:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['convert_euro'])
async def convert_euro(call: types.CallbackQuery):
    await ConverterForm.euro.set()
    await call.answer('Введіть кількість € для конвертування в долари та гривні...')


@dp.message_handler(state=ConverterForm.euro)
async def process_euro(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(
            f'Вартість покупки євро в гривнях: '
            f'{answer / cc.find_euros_buy_in_hryvnias():.4f}\n'
            f'Вартість продажі євро в гривнях: '
            f'{answer / cc.find_euros_sale_in_hryvnias():.4f}\n'
            f'Вартість покупки євро в доларах: '
            f'{answer / cc.find_euros_buy_in_dollars():.4f}\n'
            f'Вартість продажі євро в доларах: '
            f'{answer / cc.find_euros_sale_in_dollars():.4f}\n',
        )
    except ValueError:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['convert_hryvnia'])
async def convert_hryvnia(call: types.CallbackQuery):
    await ConverterForm.hryvnia.set()
    await call.answer('Введіть кількість ₴ для конвертування в долари та євро...')


@dp.message_handler(state=ConverterForm.hryvnia)
async def process_hryvnia(message: types.Message, state: FSMContext):
    input_data = message.text

    try:
        answer = float(input_data)
        await message.reply(
            f'Вартість покупки гривні в доларах: '
            f'{answer / cc.find_hryvnias_buy_in_dollars():.4f}\n'
            f'Вартість продажі гривні в доларах: '
            f'{answer / cc.find_hryvnias_sale_in_dollars():.4f}\n'
            f'Вартість покупки гривні в євро: '
            f'{answer / cc.find_hryvnias_buy_in_euros():.4f}\n'
            f'Вартість продажі гривні в євро: '
            f'{answer / cc.find_hryvnias_sale_in_euros():.4f}\n',
        )
    except ValueError:
        await message.reply('Число вказано невірно.')

    await state.finish()


@dp.callback_query_handler(text=['back_to_menu'])
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.edit_text('Виберіть опцію меню💵:', reply_markup=currency_keyboard)
    await call.answer()
