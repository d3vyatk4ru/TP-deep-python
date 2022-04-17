
class Integer:
    ''' Integer value '''
    def __init__(self) -> None:
        self.__data = 0

    def __get__(self, obj, objtype) -> int:
        return self.__data

    def __set__(self, obj, val) -> None:

        if not isinstance(val, int):
            raise Exception('Not integer value')

        self.__data = val


class String:
    ''' String value '''
    def __init__(self) -> None:
        self.__data = 0

    def __get__(self, obj, objtype) -> int:
        return self.__data

    def __set__(self, obj, val) -> None:

        if not isinstance(val, str):
            raise Exception('Not str value')

        self.__data = val


class PositiveInteger:
    ''' Positive integer value '''
    def __init__(self) -> None:
        self.__data = 0

    def __get__(self, obj, objtype) -> int:
        return self.__data

    def __set__(self, obj, val) -> None:

        if not isinstance(val, int):
            raise Exception('Not integer value')

        if val < 0:
            raise Exception('Not positive value')

        self.__data = val


class Data:
    ''' Study descriptor protocol '''
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num: Integer, name: String,
                 price: PositiveInteger) -> None:
        self.num = num
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'num: {self.num}, name: {self.name}, price: {self.price}'

    def __repr__(self) -> str:
        return f'num: {self.num}, name: {self.name}, price: {self.price}'
