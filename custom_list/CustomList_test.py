import unittest
from CustomList import CustomList


class CustomListTest(unittest.TestCase):

    def test_sum_2_custom_list_eq_len(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12])

    def test_sum_2_custom_list_not_eq_len_first(self):

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sum_2_custom_list_not_eq_len_second(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sum_custom_list_std_list_first_eq_len(self):

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12])

    def test_sum_custom_list_std_list_first_not_eq_len_1(self):

        list1 = [1, 2, 3, 4, 5]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sum_custom_list_std_list_first_not_eq_len_2(self):

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sum_custom_list_std_list_second_eq_len(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8]
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12])

    def test_sum_custom_list_std_list_second_not_eq_len_1(self):

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = [5, 6, 7, 8]
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sum_custom_list_std_list_second_not_eq_len_2(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8, 5]
        tmp = list1 + list2

        self.assertListEqual(tmp._CustomList__data, [6, 8, 10, 12, 5])

    def test_sub_2_custom_list_eq_len(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4])

    def test_sub_2_custom_list_not_eq_len_first(self):

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, 5])

    def test_sub_2_custom_list_not_eq_len_second(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, -5])

    def test_sub_custom_list_std_list_first_eq_len(self):

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4])

    def test_sub_custom_list_std_list_first_not_eq_len_1(self):

        list1 = [1, 2, 3, 4, 5]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, 5])

    def test_sub_custom_list_std_list_first_not_eq_len_2(self):

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, -5])

    def test_sub_custom_list_std_list_second_eq_len(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8]
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4])

    def test_sub_custom_list_std_list_second_not_eq_len_1(self):

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = [5, 6, 7, 8]
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, 5])

    def test_sub_custom_list_std_list_second_not_eq_len_2(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8, 5]
        tmp = list1 - list2

        self.assertListEqual(tmp._CustomList__data, [-4, -4, -4, -4, -5])

    def test_len_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertEqual(len(list1), 4)

    def test_next_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        list1_iter = iter(list1)

        self.assertEqual(next(list1_iter), 1)
        self.assertEqual(next(list1_iter), 2)
        self.assertEqual(next(list1_iter), 3)
        self.assertEqual(next(list1_iter), 4)

    def test_str_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertEqual(str(list1), 'CustomList([1, 2, 3, 4]) 10')

    def test_eq_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([5, 6, 7, 8, 5])

        self.assertFalse(list1 == list2)

    def test_neg_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertListEqual((-list1)._CustomList__data, [-1, -2, -3, -4])

    def test_neg_list(self):

        list1 = [1, 2, 3, 4]

        self.assertListEqual(CustomList._CustomList__neg_list(list1),
                             [-1, -2, -3, -4])

    def test_getitem_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertEqual(list1[0], 1)
        self.assertEqual(list1[1], 2)
        self.assertEqual(list1[2], 3)
        self.assertEqual(list1[3], 4)

    def test_make_add(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([4, 3, 2, 1])

        self.assertListEqual(CustomList._CustomList__make_add(list1, list2),
                             [5, 5, 5, 5])

    def test_append_zero(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertListEqual(CustomList._CustomList__append_zero(list1, 5),
                             CustomList([1, 2, 3, 4, 0]))

    def test_eq_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 == list2)

    def test_lt_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertTrue(list1 < list2)

    def test_lt_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertFalse(list2 < list1)

    def test_gt_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertFalse(list1 > list2)

    def test_gt_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertTrue(list2 > list1)

    def test_ne_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertTrue(list1 != list2)

    def test_ne_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertFalse(list2 != list1)

    def test_le_custom_list_true1(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 <= list2)

    def test_le_custom_list_true2(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertTrue(list1 <= list2)

    def test_le_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 5])

        self.assertFalse(list2 <= list1)

    def test_ge_custom_list_true1(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 >= list2)

    def test_ge_custom_list_true2(self):

        list1 = CustomList([1, 2, 3, 5])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 >= list2)

    def test_ge_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 5])

        list2 = CustomList([1, 2, 3, 4])

        self.assertFalse(list2 >= list1)


if __name__ == "__main__":

    unittest.main()
