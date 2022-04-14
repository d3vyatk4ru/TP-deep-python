from typing import List, Iterable


class NotSupportedType(Exception):
    """Исключение для типов не являющихся CustomList и list"""

    def __init__(self, message: str =
                 "Type is not include in CustomList and list") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.message}'


class CustomList(list):
    """ Реализация кастомного списка поверх стандартного list """

    def __init__(self, data: Iterable[float]) -> None:
        super().__init__()
        self.__data = data
        self.__list_iter = None

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> object:
        self.__list_iter = iter(self.__data)
        return self

    def __next__(self) -> float:
        return next(self.__list_iter)

    def __str__(self) -> str:
        return f'CustomList({self.__data}) {sum(self.__data)}'

    def __getitem__(self, key: int) -> float:
        return self.__data[key]

    @classmethod
    def __make_add(cls, this: object, __o: object) -> object:

        return cls([x + y for (x, y) in zip(this, __o)])

    @staticmethod
    def __append_zero(small_list: object, len_big_list: int) -> object:

        result = small_list[:]

        while len(result) < len_big_list:
            result.append(0)

        return result

    def __add__(self, __o) -> object:

        if not isinstance(__o, list) and not isinstance(__o, CustomList):
            raise NotSupportedType

        if len(self) > len(__o):
            return self.__make_add(self.__append_zero(__o, len(self)), self)

        if len(self) < len(__o):
            return self.__make_add(self.__append_zero(self, len(__o)), __o)

        return self.__make_add(self, __o)

    def __radd__(self, __o: object) -> object:
        return self + __o

    def __neg__(self) -> object:
        self.__data = list(map(lambda x: -x, self))
        return self

    @staticmethod
    def __neg_list(obj: List[float]) -> List[float]:
        return list(map(lambda x: -x, obj))

    def __sub__(self, __o: object) -> object:

        if isinstance(__o, CustomList):
            return self.__add__(-__o)

        if isinstance(__o, list):
            return self.__add__(self.__neg_list(__o))

        return None

    def __rsub__(self, __o: object) -> object:
        return -self + __o

    def __eq__(self, __o: object) -> bool:
        return sum(self) == sum(__o)

    def __lt__(self, __o: object) -> bool:
        return sum(self) < sum(__o)

    def __gt__(self, __o: object) -> bool:
        return sum(self) > sum(__o)

    def __ne__(self, __o: object) -> bool:
        return sum(self) != sum(__o)

    def __le__(self, __o: object) -> bool:
        return sum(self) <= sum(__o)

    def __ge__(self, __o: object) -> bool:
        return sum(self) >= sum(__o)
