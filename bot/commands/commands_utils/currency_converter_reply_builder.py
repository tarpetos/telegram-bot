from typing import Type, Literal, List

Currency: Type[str] = Literal["dollars", "hryvnias", "euros", "bitcoins"]


def currency_reply(
        currency_amount: float,
        input_data: str,
        main_currency: Currency,
        exchange_currency: List[Currency],
        buy_price: List[float],
        sell_price: List[float],
) -> str:
    return "".join(
        f"Cost of buying {input_data} {main_currency} in {exchange_currency[index]}: "
        f"{currency_amount / buy_price[index]:.4f}\n"
        f"Selling price of {input_data} {main_currency} in {exchange_currency[index]}: "
        f"{currency_amount / sell_price[index]:.4f}\n\n"
        for index in range(len(buy_price))
    )
