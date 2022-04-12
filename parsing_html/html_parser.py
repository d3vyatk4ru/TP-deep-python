from typing import List
from collections import deque

OPEN_BRACKET = '<'
CLOSE_BRACKET = '>'


def parse_html(html_str: str, open_tag_callback, data_callback,
               close_tag_callback) -> List[str]:
    """
    Делаем парсинг html
    """

    stack_data = deque()

    idx: int = 0

    while idx < len(html_str) - 1:

        if html_str[idx] == OPEN_BRACKET and html_str[idx + 1] != '/':

            tag_name = get_tag_name(html_str, idx + 1)

            idx += len(tag_name) + 1

            open_tag_callback(tag_name)

            stack_data.append("")

            continue

        if html_str[idx] == OPEN_BRACKET and html_str[idx + 1] == '/':

            tag_name = get_tag_name(html_str, idx + 2)

            idx += len(tag_name) + 2

            data_callback(stack_data.pop())

            close_tag_callback(tag_name)

            continue

        data: str = get_data(html_str, idx + 1)

        idx += len(data) + 1

        stack_data[-1] += data


def get_tag_name(html_str: str, idx: int) -> str:

    """
    Получаем имя тэга
    """

    tag_name: str = ""

    while html_str[idx] != CLOSE_BRACKET:

        tag_name += html_str[idx]
        idx += 1

    return tag_name


def get_data(html_str: str, idx: int) -> str:

    """
    Получаем данные внутри тэга.
    """

    data: str = ""

    while html_str[idx] != OPEN_BRACKET:

        data += html_str[idx]
        idx += 1

    return data


def fopen_callback(string):
    """
    Something docstring.
    """
    return string


def fclose_callback(string):
    """
    Something docstring.
    """
    return string


def fdata_callback(string):
    """
    Something docstring.
    """
    return string


if __name__ == "__main__":

    parse_html("<abc>Hi<def>lol</def>world</abc>", fopen_callback,
               fdata_callback, fclose_callback)
