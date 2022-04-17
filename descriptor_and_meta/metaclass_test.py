import unittest
from metaclass import CustomClass

class TestCustomClass(unittest.TestCase):

    def test_real__attr_name_raise(self):

        inst = CustomClass()

        self.assertFalse(hasattr(CustomClass, 'x'))

        with self.assertRaises(AttributeError):
            inst.x

    def test_real_method_name_raise(self):

        inst = CustomClass()

        self.assertFalse(hasattr(CustomClass, 'line'))

        with self.assertRaises(AttributeError):
            inst.line

    def test_real_static_method_name_raise(self):

        inst = CustomClass()

        self.assertFalse(hasattr(CustomClass, 'return_9'))

        with self.assertRaises(AttributeError):
            inst.return_9

    def test_real_method_name_with_underline_raise(self):

        inst = CustomClass()

        self.assertFalse(hasattr(CustomClass, 'return_100__'))

        with self.assertRaises(AttributeError):
            inst.return_100__()

    def test_custom_prefix_attr(self):

        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, 'custom_x'))

        self.assertEqual(inst.custom_x, 50)

    def test_custom_prefix_method(self):

        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, 'custom_line'))

        self.assertEqual(inst.custom_line(), 99)

    def test_custom_prefix_name_with_underline_method(self):

        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, 'custom_return_100__'))

        self.assertEqual(inst.custom_return_100__(), 100)

    def test_custom_prefix_static_method(self):

        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, 'custom_return_9'))

        self.assertEqual(inst.custom_return_9(), 9)

    def test_attr_from_cls(self):

        with self.assertRaises(AttributeError):
            CustomClass.line()

    def test_method_from_cls(self):

        with self.assertRaises(AttributeError):
            CustomClass.x

    def test_dunder_method(self):

        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, '__str__'))

        self.assertEqual(inst.__str__(), "Custom_by_metaclass")

    def test_instance_attr_raise(self):

        inst = CustomClass()

        self.assertFalse(hasattr(inst, 'val'))

        with self.assertRaises(AttributeError):
            inst.val

    def test_instance_attr(self):

        inst = CustomClass()

        self.assertTrue(hasattr(inst, 'custom_val'))

        self.assertEqual(inst.custom_val, 99)
    

if __name__ == '__main__':
    unittest.main()