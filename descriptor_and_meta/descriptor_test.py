import unittest

from descriptor import Data

class TestData(unittest.TestCase):

    def test_good_value(self):

        d = Data(-100, 'abc', 22)

        self.assertEqual(d.num, -100)
        self.assertEqual(d.name, 'abc')
        self.assertEqual(d.price, 22)
    
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

        d = Data(100, 'abc', 1)

        self.assertEqual(str(d), 'num: 100, name: abc, price: 1')

    def test_repe_method(self):

        d = Data(100, 'abc', 1)

        self.assertEqual(str(d), 'num: 100, name: abc, price: 1')


if __name__ == '__main__':

    unittest.main()