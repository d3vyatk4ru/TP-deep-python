from typing import List

class NotSupportedType(Exception):
    """Исключение для типов не являющихся CustomList и list"""

    def __init__(self, message: str = "Type is not include in CustomList and list") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.message}'


class CustomList(list):
    """ Реализация кастомного списка поверх стандартного list """

    def __init__(self, data: List[float]) -> None:
        super().__init__()
        self.__data = data
        self.__list_iter = None

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> object:
        self.__list_iter = iter(self.__data)
        return self

    def __next__(self):
        return next(self.__list_iter)

    def __str__(self) -> str:
        return f'CustomList({self.__data}) {sum(self.__data)}'

    def __getitem__(self, key):
        return self.__data[key]

    @classmethod
    def __make_add(cls, this: List[float], other: List[float]) -> object:

        return cls([x + y for (x, y) in zip(this, other)])

    def __append_zero(self, small_list, big_list) -> object:

        result = small_list[:]

        while len(result) < len(big_list):
            result.append(0)

        return self.__make_add(result, big_list)


    def __add__(self, __o) -> object:

        if not isinstance(__o, list) and not isinstance(__o, CustomList):
            raise NotSupportedType

        if len(self) > len(__o):
            return self.__append_zero(__o, self)

        if len(self) < len(__o):
            return self.__append_zero(self, __o)

        return self.__make_add(self, __o)

    def __radd__(self, __o: object) -> object:
        return self + __o

    def __neg__(self) -> object:
        self.__data = list(map(lambda x: -x, self.__data))
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

    def __rsub__(self, other):
        return -self + other

    def __eq__(self, __o: object) -> bool:
        return sum(self) == sum(__o)
        

if __name__ == '__main__':

    list1 = CustomList([1, 2, 3, 4])
    list2 = CustomList([5, 6, 7, 8, 5])

    a = list1 + list2

    print(a)
