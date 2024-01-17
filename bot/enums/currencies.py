from enum import Enum, auto
from typing import Type, Literal


class Currency(str, Enum):
    HRYVNIAS = auto()
    DOLLARS = auto()
    EUROS = auto()
    BITCOINS = auto()

    def __str__(self) -> str:
        return self.name.lower()

    @classmethod
    def __len__(cls) -> int:
        return len(cls._member_names_)


# CurrencyType: Type[Currency] = Literal[Currency.DOLLARS, Currency.HRYVNIAS, Currency.EUROS, Currency.BITCOINS]
