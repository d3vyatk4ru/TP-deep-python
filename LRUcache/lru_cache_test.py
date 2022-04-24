import unittest
from lru_cache import LRUCache

class LRUCacheTest(unittest.TestCase):

    def test_set_value(self):

        cache = LRUCache(2)

        self.assertTrue(cache.set('k1', 'val1'))
        self.assertTrue(cache.set('k2', 'val2'))

    def test_set_get_value(self):

        cache = LRUCache(2)

        self.assertTrue(cache.set('k1', 'val1'))
        self.assertTrue(cache.set('k2', 'val2'))

        self.assertEqual(cache.get('k1'), 'val1')
        self.assertEqual(cache.get('k2'), 'val2')

    def test_set_larger_limit(self):

        cache = LRUCache(2)

        self.assertTrue(cache.set('k1', 'val1'))
        self.assertTrue(cache.set('k2', 'val2'))

        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'val1')

        self.assertTrue(cache.set('k3', 'val3'))

        self.assertEqual(cache.get('k3'), 'val3')
        self.assertEqual(cache.get('k2'), None)
        self.assertEqual(cache.get('k1'), 'val1')

    def test_overwrite(self):

        cache = LRUCache(2)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')

        cache.set('k1', 'new_val1')

        self.assertEqual(cache.get('k1'), 'new_val1')

    def test_order_overwrite(self):

        cache = LRUCache(2)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')

        self.assertEqual(str(cache), ' -> [k2, val2] -> [k1, val1] ->')

        cache.set('k1', 'new_val1')

        self.assertEqual(str(cache), ' -> [k1, new_val1] -> [k2, val2] ->')

    def test_order(self):

        size = 2

        cache = LRUCache(size)

        for i in range(size):
            cache.set(f'k{i}', f'val{i}')

        self.assertEqual(str(cache), ' -> [k1, val1] -> [k0, val0] ->')

if __name__ == '__main__':
    unittest.main()
