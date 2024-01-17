from typing import Dict, Union, Tuple, List

from aiogram import types
from aiogram.dispatcher import FSMContext

from .commands_utils.currency_converter_reply_builder import currency_reply
from .commands_utils.currency_cost import Converter
# from .commands_utils.currency_cost import get_currency_rate_data
from .commands_utils.states import ConverterForm
from .commands_utils import currency_cost as cc
from ..config import dp, CURRENCY_URL
from ..enums import Command
from ..enums.currencies import Currency
# from ..enums.currencies import CurrencyType
from ..enums.keyboard_callbacks import ConverterCallbackStorage
from ..keyboards.currency_converter_keyboard import main_converter_menu, currency_rate_menu, convert_menu
from ..keyboards.keyboard_close import close_keyboard


@dp.message_handler(state="*", commands=Command.CURRENCY_CONVERTER)
async def currency_command_handler(message: types.Message):
    await message.reply("Choose menu option💵:", reply_markup=main_converter_menu)


@dp.callback_query_handler(text=ConverterCallbackStorage.CURRENCY_RATE)
async def process_exchange_rate(call: types.CallbackQuery):
    rate_data = cc.get_currency_rate_data(CURRENCY_URL)
    # bitcoin = get_currency_rate_data(BITCOIN_URL)

    await call.message.edit_text(
        f"<b><i>BUY / SALE</i></b>\n"
        f"<code>"
        f"1 UAH = {cc.find_dollars_buy_in_hryvnias(rate_data):.4f} / {cc.find_dollars_sale_in_hryvnias(rate_data):.4f} USD\n"
        f"1 UAH = {cc.find_euros_buy_in_hryvnias(rate_data):.4f} / {cc.find_euros_sale_in_hryvnias(rate_data):.4f} EUR\n"
        f"1 EUR = {cc.find_dollars_buy_in_euros(rate_data):.4f} / {cc.find_dollars_sale_in_euros(rate_data):.4f} USD\n"
        f"1 EUR = {cc.find_hryvnias_buy_in_euros(rate_data):.4f} / {cc.find_hryvnias_sale_in_euros(rate_data):.4f} UAH\n"
        f"1 USD = {cc.find_euros_buy_in_dollars(rate_data):.4f} / {cc.find_euros_sale_in_dollars(rate_data):.4f} EUR\n"
        f"1 USD = {cc.find_hryvnias_buy_in_dollars(rate_data):.4f} / {cc.find_hryvnias_sale_in_dollars(rate_data):.4f} UAH\n"
        # f"1 BTC = {cc.bitcoin_price_in_dollars(bitcoin):.4f} USD\n"
        # f"1 BTC = {cc.bitcoin_price_in_euros(bitcoin):.4f} EUR\n"
        f"</code>",
        parse_mode="HTML",
        reply_markup=currency_rate_menu,
    )
    await call.answer()


@dp.callback_query_handler(text=ConverterCallbackStorage.CURRENCY_CONVERTER)
async def process_converter(call: types.CallbackQuery):
    await call.message.edit_text("Currency converter:", reply_markup=convert_menu)
    await call.answer()


@dp.callback_query_handler(text=ConverterCallbackStorage.CONVERT_DOLLAR)
async def convert_dollar(call: types.CallbackQuery):
    await ConverterForm.dollar.set()
    await call.answer(
        "Enter the amount of $ to convert into euros and hryvnias...", True
    )


@dp.message_handler(state=ConverterForm.dollar)
async def process_dollar(message: types.Message, state: FSMContext):
    ...
    # rate_data = get_currency_rate_data(CURRENCY_URL)
    #
    # data: Dict[str, Union[Currency, Tuple[Currency, Currency], Tuple[float, float]]] = {
    #     "main_currency": "dollars",
    #     "exchange_currency": ("hryvnias", "euros"),
    #     "buy_price": (cc.find_dollars_buy_in_hryvnias(rate_data), cc.find_dollars_buy_in_euros(rate_data)),
    #     "sell_price": (cc.find_dollars_sale_in_hryvnias(rate_data), cc.find_dollars_sale_in_euros(rate_data)),
    # }
    # await process_currency(message, state, reply_data=data)


@dp.callback_query_handler(text=ConverterCallbackStorage.CONVERT_EURO)
async def convert_euro(call: types.CallbackQuery):
    await ConverterForm.euro.set()
    await call.answer(
        "Enter the amount of € to convert to dollars and hryvnias...", True
    )


@dp.message_handler(state=ConverterForm.euro)
async def process_euro(message: types.Message, state: FSMContext):
    ...
    # rate_data = get_currency_rate_data(CURRENCY_URL)
    #
    # data: Dict[str, Union[Currency, Tuple[Currency, Currency], Tuple[float, float]]] = {
    #     "main_currency": "euros",
    #     "exchange_currency": ("hryvnias", "dollars"),
    #     "buy_price": (cc.find_euros_buy_in_hryvnias(rate_data), cc.find_euros_buy_in_dollars(rate_data)),
    #     "sell_price": (cc.find_euros_sale_in_hryvnias(rate_data), cc.find_euros_sale_in_dollars(rate_data)),
    # }
    # await process_currency(message, state, reply_data=data)


@dp.callback_query_handler(text=ConverterCallbackStorage.CONVERT_HRYVNIA)
async def convert_hryvnia(call: types.CallbackQuery):
    await ConverterForm.hryvnia.set()
    await call.answer("Enter the amount of ₴ to convert to dollars and euros...", True)


@dp.message_handler(state=ConverterForm.hryvnia)
async def process_hryvnia(message: types.Message, state: FSMContext):
    await process_currency(message, state, base_currency=Currency.HRYVNIAS)


async def process_currency(
        message: types.Message,
        state: FSMContext,
        base_currency: Currency
) -> None:
    input_data = message.text

    try:
        input_data = input_data.replace(",", ".")
        currency_amount = float(input_data)
        reply_dict = Converter().convert(base_currency)
        reply_data = currency_reply(
            currency_amount,
            input_data,
            *reply_dict.values(),
        )

        await message.reply(reply_data)
    except ValueError:
        await message.reply("Invalid input. Must be a number. Try again.")

    await state.finish()


@dp.callback_query_handler(text=ConverterCallbackStorage.MAIN_CONVERTER_MENU_BACK)
async def back_to_main_converter_menu(call: types.CallbackQuery):
    await call.message.edit_text("Choose menu option💵:", reply_markup=main_converter_menu)
    await call.answer()


@dp.callback_query_handler(text=ConverterCallbackStorage.CLOSE_CONVERTER)
async def close_converter(call: types.CallbackQuery):
    await close_keyboard(call)
