import unittest

from descriptor import Data


class TestData(unittest.TestCase):

    def test_good_value(self):

        data = Data(-100, 'abc', 22)

        self.assertEqual(data.num, -100)
        self.assertEqual(data.name, 'abc')
        self.assertEqual(data.price, 22)

    def test_bad_num(self):

        with self.assertRaises(Exception):
            _ = Data('def', 'abc', 22)

    def test_bad_name(self):

        with self.assertRaises(Exception):
            _ = Data(100, 992992, 22)

    def test_bad_price(self):

        with self.assertRaises(Exception):
            _ = Data(100, 'abc', -1)

    def test_str_method(self):

        data = Data(100, 'abc', 1)

        self.assertEqual(str(data), 'num: 100, name: abc, price: 1')

    def test_repe_method(self):

        data = Data(100, 'abc', 1)

        self.assertEqual(str(data), 'num: 100, name: abc, price: 1')

    def test_new_value_num_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.num = 'a'

    def test_new_value_num_check_prev_val_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.num = 'a'

        self.assertEqual(data.num, 100)

    def test_new_num_and_good(self):

        data = Data(100, 'abc', 1)
        data.num = 123
        self.assertEqual(data.num, 123)

    def test_new_value_name_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.name = 10

    def test_new_value_name_check_prev_val_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.name = 1

        self.assertEqual(data.name, 'abc')

    def test_new_name_and_check_good(self):

        data = Data(100, 'abc', 1)
        data.name = 'def'

        self.assertEqual(data.name, 'def')

    def test_new_value_price_neg_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.price = -100

    def test_new_value_price_str_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.price = 'a'

    def test_new_value_price_check_prev_val_bad(self):

        data = Data(100, 'abc', 1)
        with self.assertRaises(Exception):
            data.price = 'a'

        self.assertEqual(data.price, 1)

    def test_new_price_and_check_good(self):

        data = Data(100, 'abc', 1)
        data.price = 500

        self.assertEqual(data.price, 500)


if __name__ == '__main__':
    unittest.main()
