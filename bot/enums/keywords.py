from enum import Enum


class Keyword(str, Enum):


    @classmethod
    def __len__(cls) -> int:
        return len(cls._member_names_)
