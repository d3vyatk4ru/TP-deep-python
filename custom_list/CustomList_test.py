import unittest
from CustomList import CustomList, NotSupportedType


class CustomListTest(unittest.TestCase):

    def test_check_init_custom_list_sum(self):

        init_list1 = [1, 2, 3, 4]
        init_list2 = [5, 6, 7, 8]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        _ = list1 + list2

        for i, _ in enumerate(init_list1):
            self.assertEqual(list1[i], init_list1[i])
            self.assertEqual(list2[i], init_list2[i])

    def test_check_init_custom_list_sub(self):

        init_list1 = [1, 2, 3, 4]
        init_list2 = [5, 6, 7, 8]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        _ = list1 - list2

        for i, _ in enumerate(init_list1):
            self.assertEqual(list1[i], init_list1[i])
            self.assertEqual(list2[i], init_list2[i])

    def custom_return_type_sum(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 + list2

        self.assertIsInstance(tmp, CustomList)

    def custom_return_type_sub(self):

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 - list2

        self.assertIsInstance(tmp, CustomList)

    def test_sum_2_custom_list_eq_len(self):

        answer = [6, 8, 10, 12]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_2_custom_list_not_eq_len_first(self):

        answer = [6, 8, 10, 12, 5]

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_2_custom_list_not_eq_len_second(self):

        answer = [6, 8, 10, 12, 5]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_first_eq_len(self):

        answer = [6, 8, 10, 12]

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_first_not_eq_len_1(self):

        answer = [6, 8, 10, 12, 5]

        list1 = [1, 2, 3, 4, 5]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_first_not_eq_len_2(self):
        
        answer = [6, 8, 10, 12, 5]

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_second_eq_len(self):

        answer = [6, 8, 10, 12]

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8]
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_second_not_eq_len_1(self):

        answer = [6, 8, 10, 12, 5]

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = [5, 6, 7, 8]
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sum_custom_list_std_list_second_not_eq_len_2(self):

        answer = [6, 8, 10, 12, 5]

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8, 5]
        tmp = list1 + list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_2_custom_list_eq_len(self):

        answer = [-4, -4, -4, -4]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_2_custom_list_not_eq_len_first(self):

        answer = [-4, -4, -4, -4, 5]

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = CustomList([5, 6, 7, 8])

        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_2_custom_list_not_eq_len_second(self):

        answer = [-4, -4, -4, -4, -5]

        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_first_eq_len(self):

        answer = [-4, -4, -4, -4]

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_first_not_eq_len_1(self):

        answer = [-4, -4, -4, -4, 5]

        list1 = [1, 2, 3, 4, 5]
        list2 = CustomList([5, 6, 7, 8])
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_first_not_eq_len_2(self):

        answer = [-4, -4, -4, -4, -5]

        list1 = [1, 2, 3, 4]
        list2 = CustomList([5, 6, 7, 8, 5])
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_second_eq_len(self):

        answer = [-4, -4, -4, -4]

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8]
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_second_not_eq_len_1(self):

        answer = [-4, -4, -4, -4, 5]

        list1 = CustomList([1, 2, 3, 4, 5])
        list2 = [5, 6, 7, 8]
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_sub_custom_list_std_list_second_not_eq_len_2(self):

        answer = [-4, -4, -4, -4, -5]

        list1 = CustomList([1, 2, 3, 4])
        list2 = [5, 6, 7, 8, 5]
        tmp = list1 - list2

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_str_custom_list(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertEqual(str(list1), 'CustomList([1, 2, 3, 4]) 10')

    def test_eq_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([5, 6, 7, 8, 5])

        self.assertFalse(list1 == list2)

    def test_neg_custom_list(self):

        answer = [-1, -2, -3, -4]

        list1 = CustomList([1, 2, 3, 4])

        tmp = -list1

        self.assertEqual(len(tmp), len(answer))

        for i, _ in enumerate(answer):
            self.assertEqual(tmp[i], answer[i])

    def test_neg_list(self):

        list1 = [1, 2, 3, 4]

        self.assertListEqual(CustomList._CustomList__neg_list(list1),
                             [-1, -2, -3, -4])

    def test_make_add(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([4, 3, 2, 1])

        self.assertListEqual(CustomList._CustomList__make_add(list1, list2),
                             [5, 5, 5, 5])

    def test_append_zero(self):

        list1 = CustomList([1, 2, 3, 4])

        self.assertListEqual(CustomList._CustomList__append_zero(list1, 5),
                             CustomList([1, 2, 3, 4, 0]))

    def test_eq_custom_list_true_equal_size(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 == list2)

    def test_eq_custom_list_true_not_equal_size(self):

        list1 = CustomList([1, 2, 3, 4, 0])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 == list2)

    def test_eq_custom_list_false_equal_size(self):

        list1 = CustomList([1, 2, 3, 10])

        list2 = CustomList([1, 2, 3, 4])

        self.assertFalse(list1 == list2)

    def test_eq_custom_list_false_not_equal_size(self):

        list1 = CustomList([1, 2, 3, 10, 0])

        list2 = CustomList([1, 2, 3, 4])

        self.assertFalse(list1 == list2)

    def test_lt_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

        self.assertTrue(list1 < list2)

    def test_lt_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

        self.assertFalse(list2 < list1)

    def test_gt_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

        self.assertFalse(list1 > list2)

    def test_gt_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

        self.assertTrue(list2 > list1)

    def test_ne_custom_list_true(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

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

        list2 = CustomList([1, 2, 3, 10])

        self.assertTrue(list1 <= list2)

    def test_le_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 10])

        self.assertFalse(list2 <= list1)

    def test_ge_custom_list_true1(self):

        list1 = CustomList([1, 2, 3, 4])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 >= list2)

    def test_ge_custom_list_true2(self):

        list1 = CustomList([1, 2, 3, 10])

        list2 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 >= list2)

    def test_ge_custom_list_false(self):

        list1 = CustomList([1, 2, 3, 10])

        list2 = CustomList([1, 2, 3, 4])

        self.assertFalse(list2 >= list1)

    def test_check_exception(self):

        self.assertRaises(CustomList(1), NotSupportedType)


if __name__ == "__main__":

    unittest.main()
