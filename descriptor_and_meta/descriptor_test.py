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

    def test_new_value_num_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.num = 'a'

    def test_new_value_num_check_prev_val_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.num = 'a'

        self.assertEqual(d.num, 100)

    def test_new_num_and_good(self):

        d = Data(100, 'abc', 1)
        
        d.num = 123

        self.assertEqual(d.num, 123)

    def test_new_value_name_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.name = 10

    def test_new_value_name_check_prev_val_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.name = 1

        self.assertEqual(d.name, 'abc')

    def test_new_name_and_check_good(self):

        d = Data(100, 'abc', 1)
        d.name = 'def'

        self.assertEqual(d.name, 'def')

    def test_new_value_price_neg_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.price = -100

    def test_new_value_price_str_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.price = 'a'

    def test_new_value_price_check_prev_val_bad(self):

        d = Data(100, 'abc', 1)
        
        with self.assertRaises(Exception):
            d.price = 'a'

        self.assertEqual(d.price, 1)

    def test_new_price_and_check_good(self):

        d = Data(100, 'abc', 1)
        d.price = 500

        self.assertEqual(d.price, 500)


if __name__ == '__main__':

    unittest.main()