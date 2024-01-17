import json
from abc import ABC, abstractmethod
from typing import Any, Union, Dict, List, Tuple
from urllib.request import urlopen

import requests

# from bot.config import CURRENCY_URL, BITCOIN_URL
from bot.enums.currencies import Currency


# from .currency_converter_reply_builder import Currency


class Converter:
    CURRENCY_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=11"
    BITCOIN_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

    def _fetch_url_data(self, url: str) -> Any:
        response = urlopen(url)
        currency_rate_data = json.loads(response.read())
        return currency_rate_data

    def fetch_currency_data(self) -> Dict[str, Dict[str, float]]:
        data = self._fetch_url_data(self.CURRENCY_URL)
        return {
            "buy": {
                "uah_eur": float(data[0]["buy"]),
                "uah_usd": float(data[1]["buy"]),
            },
            "sale": {
                "uah_eur": float(data[0]["sale"]),
                "uah_usd": float(data[1]["sale"]),
            },
        }

    def fetch_bitcoin_data(self) -> Dict[str, float]:
        data = self._fetch_url_data(self.BITCOIN_URL)
        return {
            "btc_usd": float(data["bpi"]["USD"]["rate_float"]),
        }

    def united_currency_data(self) -> Dict[str, Dict[str, float]]:
        main_data = self.fetch_currency_data()
        crypto_data = self.fetch_bitcoin_data()
        main_data["buy"]["uah_btc"] = crypto_data["btc_usd"] * main_data["buy"]["uah_usd"]
        main_data["sale"]["uah_btc"] = crypto_data["btc_usd"] * main_data["sale"]["uah_usd"]

        return main_data

    def convert(
            self, base_currency: Currency
    ) -> Dict[str, Union[Currency, List[Currency], List[float]]]:
        currency_list = [*Currency]
        currency_list.remove(base_currency)

        currency_data = {
            "main_currency": base_currency,
            "exchange_currency": currency_list,
        }

        convert_data = self.united_currency_data()
        print(convert_data["buy"].values())
        print(convert_data["sale"].values())

        if base_currency == Currency.HRYVNIAS:
            currency_data["buy_price"] = list(convert_data["buy"].values())
            currency_data["sale_price"] = list(convert_data["sale"].values())
        elif base_currency == Currency.DOLLARS:
            currency_data["buy_price"] = [1, 1, 1]
            currency_data["sale_price"] = [1, 1, 1]
        elif base_currency == Currency.EUROS:
            currency_data["buy_price"] = [1, 1, 1]
            currency_data["sale_price"] = [1, 1, 1]
        elif base_currency == Currency.BITCOINS:
            currency_data["buy_price"] = [1, 1, 1]
            currency_data["sale_price"] = [1, 1, 1]

        return currency_data


# print(Converter().unite_currency_data())
# class Converter:
#     def __init__(self):
#         self.currency_rate_data = self._get_currency_rate_data(CURRENCY_URL)
#         self.crypto_rate_data = self._get_currency_rate_data(BITCOIN_URL)
#         self._parse_currency_url()
#         self.buy_prices_usd = {}
#         self.sale_prices_usd = {}
#
#     def _get_currency_rate_data(self, url: str) -> Any:
#         response = urlopen(url)
#         currency_rate_data = json.loads(response.read())
#         return currency_rate_data
#
#     def _parse_currency_url(self) -> None:
#         self.buy_prices_usd
#
#     def _parse_crypto_url(self) -> None:
#         ...
#
#     def convert(
#             self, converting_currency: CurrencyType
#     ) -> Dict[str, Union[CurrencyType, List[CurrencyType], List[float]]]:
#         input_data = self.check_currency_type(converting_currency)
#
#         return {
#             "main_currency": input_data["converting_currency"],
#             "exchange_currency": input_data["currency_list"],
#             "buy_price": [1, 1, 1],
#             "sell_price": [1, 1, 1],
#         }
#
#     def check_currency_type(
#             self, converting_currency: CurrencyType
#     ) -> Dict[str, Union[CurrencyType, List[CurrencyType]]]:
#         currency_list = [*Currency]
#         currency_list.remove(converting_currency)
#
#         return {
#             "converting_currency": converting_currency,
#             "currency_list": currency_list,
#         }
#
#
# Converter().convert(Currency.HRYVNIAS)

# class Converter(ABC):
#     def __init__(self, url: str):
#         self.response = urlopen(url)
#         self.currency_rate_data = json.loads(self.response.read())
#
#     @abstractmethod
#     def convert(self, currency: Currency) -> Dict[str, Union[Currency, List[Currency], List[float]]]:
#         raise NotImplementedError
#
#     @abstractmethod
#     def check_currency_type(self) -> None:
#         raise NotImplementedError
#
#
# class DefaultConverter(Converter):
#     def convert(self, currency: Currency) -> float:
#         data = {
#             "hryvnias": {
#                 "sale_usd": 12,
#                 "sale_eur": 12,
#                 "buy_usd": 12,
#                 "buy_eur": 11,
#             },
#             "dollars": {
#                 "sale_uah": 12,
#                 "sale_eur": 12,
#                 "buy_uah": 1 / float(self.currency_rate_data[1]["buy"]),
#                 "buy_eur": 11,
#             },
#             "euros": {
#                 "sale_uah": 12,
#                 "sale_usd": 12,
#                 "buy_uah": 1 / float(self.currency_rate_data[0]["buy"]),
#                 "buy_usd": 11,
#             }
#         }


# class BitcoinConverter(Converter):
#     def convert(self, currency: Crypto) -> float:
#         data = {
#             "bitcoins": {
#                 "uah": 12,
#                 "usd": 12,
#                 "eur": 12,
#             },
#         }


# def get_currency_rate_data(url: str) -> Any:
#     response = urlopen(url)
#     currency_rate_data = json.loads(response.read())
#     return currency_rate_data
#
#
# def find_dollars_buy_in_hryvnias(currency_rate_data: Any) -> float:
#     return 1 / float(currency_rate_data[1]["buy"])
#
#
# def find_euros_buy_in_hryvnias(currency_rate_data: Any) -> float:
#     return 1 / float(currency_rate_data[0]["buy"])
#
#
# def find_dollars_buy_in_euros(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[0]["buy"]) / float(currency_rate_data[1]["buy"])
#
#
# def find_hryvnias_buy_in_euros(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[0]["buy"])
#
#
# def find_euros_buy_in_dollars(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[1]["buy"]) / float(currency_rate_data[0]["buy"])
#
#
# def find_hryvnias_buy_in_dollars(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[1]["buy"])
#
#
# def find_dollars_sale_in_hryvnias(currency_rate_data: Any) -> float:
#     return 1 / float(currency_rate_data[1]["sale"])
#
#
# def find_euros_sale_in_hryvnias(currency_rate_data: Any) -> float:
#     return 1 / float(currency_rate_data[0]["sale"])
#
#
# def find_dollars_sale_in_euros(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[0]["sale"]) / float(currency_rate_data[1]["sale"])
#
#
# def find_hryvnias_sale_in_euros(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[0]["sale"])
#
#
# def find_euros_sale_in_dollars(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[1]["sale"]) / float(currency_rate_data[0]["sale"])
#
#
# def find_hryvnias_sale_in_dollars(currency_rate_data: Any) -> float:
#     return float(currency_rate_data[1]["sale"])
#
#
# def bitcoin_price_in_dollars(currency_rate_data: Any) -> float:
#     return float(currency_rate_data["bpi"]["USD"]["rate_float"])
#
#
# def bitcoin_price_in_euros(currency_rate_data: Any) -> float:
#     return float(currency_rate_data["bpi"]["EUR"]["rate_float"])
#
#
# def uah_to_usd(currency_rate_data: Any) -> str:
#     return "".join(
#         f"1 UAH = {find_dollars_buy_in_hryvnias(currency_rate_data):.4f} / "
#         f"{find_dollars_sale_in_hryvnias(currency_rate_data):.4f} USD\n"
#     )
#
#
# def uah_to_euro(currency_rate_data: Any) -> str:
#     return "".join(
#         f"1 UAH = {find_euros_buy_in_hryvnias(currency_rate_data):.4f} / "
#         f"{find_euros_sale_in_hryvnias(currency_rate_data):.4f} EUR\n"
#     )

# def uah_to_btc(currency_rate_data: Any) -> str:
#     return "".join(
#         f"1 UAH = {(find_dollars_buy_in_hryvnias(currency_rate_data) / bitcoin_price_in_dollars(currency_rate_data)):.4f} / "
#         f"{find_euros_sale_in_hryvnias(currency_rate_data):.4f} BTC\n"
#     )
