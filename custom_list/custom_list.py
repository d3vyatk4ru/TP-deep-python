from typing import List


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

    def __str__(self) -> str:
        return 'CustomList(' + super().__str__() + ')' + f' {sum(self)}'

    @classmethod
    def __make_add(cls, this: object, other: object) -> object:

        return cls([x + y for (x, y) in zip(this, other)])

    @staticmethod
    def __append_zero(small_list: object, len_big_list: int) -> object:

        result = small_list[:]

        while len(result) < len_big_list:
            result.append(0)

        return result

    def __add__(self, other) -> object:

        if not isinstance(other, list) and not isinstance(other, CustomList):
            raise NotSupportedType

        if len(self) > len(other):
            return self.__make_add(self.__append_zero(other, len(self)), self)

        if len(self) < len(other):
            return self.__make_add(self.__append_zero(self, len(other)), other)

        return self.__make_add(self, other)

    def __radd__(self, other: object) -> object:
        return self + other

    def __neg__(self) -> object:
        return CustomList(map(lambda x: -x, self))

    @staticmethod
    def __neg_list(obj: List[float]) -> List[float]:
        return list(map(lambda x: -x, obj))

    def __sub__(self, other: object) -> object:

        if isinstance(other, CustomList):
            return self.__add__(-other)

        if isinstance(other, list):
            return self.__add__(self.__neg_list(other))

        raise NotSupportedType

    def __rsub__(self, other: object) -> object:
        return -self.__sub__(other)

    def __eq__(self, other: object) -> bool:
        return sum(self) == sum(other)

    def __lt__(self, other: object) -> bool:
        return sum(self) < sum(other)

    def __gt__(self, other: object) -> bool:
        return sum(self) > sum(other)

    def __ne__(self, other: object) -> bool:
        return sum(self) != sum(other)

    def __le__(self, other: object) -> bool:
        return sum(self) <= sum(other)

    def __ge__(self, other: object) -> bool:
        return sum(self) >= sum(other)
