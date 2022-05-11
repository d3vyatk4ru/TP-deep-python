import unittest
from unittest.mock import patch
from collections import deque
import pathlib
import os

from faker import Faker
import html_parser

# pylint: disable=C0116

PATH2FILE = pathlib.Path('data.txt')
open(PATH2FILE, 'a', encoding='utf-8').close()

def fopen_callback(string):
    return string

def fclose_callback(string):
    return string

def fdata_callback(string):
    return string

def callback_file(string: str) -> None:
    with open(PATH2FILE, 'a') as file:
        file.write(string + '\n')

def read_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def clear_file(path: str) -> None:
    open(path, 'w').close()

def make_html(n_tags: int) -> str:

    fake = Faker()

    stack = deque()

    html = ""

    for _ in range(n_tags):

        tag = fake.name() + '_tag'
        stack.append(tag)

        html += html_parser.OPEN_BRACKET + tag + html_parser.CLOSE_BRACKET
        html += tag[:-4]

    for _ in range(n_tags):

        html += html_parser.OPEN_BRACKET + '/' + stack.pop() + html_parser.CLOSE_BRACKET

    return html

class ParserTest(unittest.TestCase):

    @patch('html_parser.parse_html')
    def test_simple_html(self, parse_html):

        html_str = "<abc>def</abc>"

        parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(parse_html.call_count, 1)

    @patch('html_parser.fopen_callback')
    def test_open_callback(self, fopen_callback):

        html_str = "<abc>def</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fopen_callback.call_count, 1)

    @patch('html_parser.fdata_callback')
    def test_close_callback(self, fdata_callback):

        html_str = "<abc>def</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fdata_callback.call_count, 1)

    @patch('html_parser.fclose_callback')
    def test_data_callback(self, fclose_callback):

        html_str = "<abc>def</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fclose_callback.call_count, 1)

    def test_simple_html_parse(self):

        answer = "abc\ndef\nabc\n"

        html_str = "<abc>def</abc>"

        html_parser.parse_html(html_str, callback_file, callback_file, callback_file)

        self.assertEqual(answer, read_file(PATH2FILE))

        clear_file(PATH2FILE)

        os.remove(PATH2FILE)

    @patch('html_parser.fopen_callback')
    def test_empty_html_open_callback(self, fopen_callback):

        html_str = ""

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fopen_callback.call_count, 0)

    @patch('html_parser.fdata_callback')
    def test_empty_html_data_callback(self, fdata_callback):

        html_str = ""

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fdata_callback.call_count, 0)

    @patch('html_parser.fclose_callback')
    def test_empty_html_close_callback(self, fclose_callback):

        html_str = ""

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fclose_callback.call_count, 0)

    def test_empty_html_parse(self):

        answer = ""

        html_str = ""

        html_parser.parse_html(html_str, callback_file, callback_file, callback_file)

        self.assertEqual(answer, read_file(PATH2FILE))

        clear_file(PATH2FILE)

        os.remove(PATH2FILE)

    @patch('html_parser.fopen_callback')
    def test_open_callback_in_3_comm(self, fopen_callback):

        html_str = "<abc>comm2<def>comm1</def>+comm3</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fopen_callback.call_count, 2)

    @patch('html_parser.fdata_callback')
    def test_data_callback_in_3_comm(self, fdata_callback):

        html_str = "<abc>comm2<def>comm1</def>+comm3</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fdata_callback.call_count, 2)

    @patch('html_parser.fclose_callback')
    def test_close_callback_in_3_comm(self, fclose_callback):

        html_str = "<abc>comm2<def>comm1</def>+comm3</abc>"

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fclose_callback.call_count, 2)

    def test_html_parse_in_3_comm(self):

        answer = "abc\ndef\ncomm1\ndef\ncomm2comm3\nabc\n"

        html_str = "<abc>comm2<def>comm1</def>comm3</abc>"

        html_parser.parse_html(html_str, callback_file, callback_file, callback_file)

        self.assertEqual(answer, read_file(PATH2FILE))

        clear_file(PATH2FILE)

        os.remove(PATH2FILE)

    def test_html_parse_2_comm(self):

        answer = "abc\ndef\ncomm1\ndef\ncomm2\nabc\n"

        html_str = "<abc>comm2<def>comm1</def></abc>"

        html_parser.parse_html(html_str, callback_file, callback_file, callback_file)

        self.assertEqual(answer, read_file(PATH2FILE))

        clear_file(PATH2FILE)

        os.remove(PATH2FILE)


    @patch('html_parser.fopen_callback')
    def test_open_callback_100_tags(self, fopen_callback):

        html_str = make_html(100)

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fopen_callback.call_count, 100)

    @patch('html_parser.fdata_callback')
    def test_data_callback_100_tags(self, fdata_callback):

        html_str = make_html(100)

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fdata_callback.call_count, 100)

    @patch('html_parser.fclose_callback')
    def test_close_callback_100_tags(self, fclose_callback):

        html_str = make_html(100)

        html_parser.parse_html(html_str, fopen_callback, fdata_callback, fclose_callback)

        self.assertEqual(fclose_callback.call_count, 100)

if __name__ == "__main__":

    unittest.main()
