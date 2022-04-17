
from typing import Dict


class CustomMeta(type):
    ''' Meta class for add 'custom_' prefix '''

    NEW_PREFIX = 'custom_'

    @staticmethod
    def add_prefix(name: str, prefix: str) -> str:
        ''' cat 2 strings '''
        return f'{prefix}{name}'

    def __new__(cls: object, name_cls: str, bases,
                clsdct: Dict, **kwargs) -> object:

        new_clsdct = {}

        for key, val in clsdct.items():

            if not (key.startswith('__') and key.endswith('__')):

                new_key = CustomMeta.add_prefix(key, CustomMeta.NEW_PREFIX)
                new_clsdct[new_key] = val
            else:
                new_clsdct[key] = val

        return super().__new__(cls, name_cls, bases, new_clsdct, **kwargs)


class CustomClass(metaclass=CustomMeta):
    ''' Inheritance by metaclass 'CustomMeta' '''
    x = 50

    def __init__(self, val: int = 99) -> None:
        self.val = val

    @staticmethod
    def line() -> int:
        ''' Return val '''
        return 99

    @staticmethod
    def return_9() -> int:
        ''' Return 9 '''
        return 9

    def __str__(self) -> str:
        return 'Custom_by_metaclass'

    def __setattr__(self, name: str, value) -> None:
        self.__dict__['custom_' + name] = value

    @staticmethod
    def return_100__():
        ''' Bla Bla Bla'''
        return 100
