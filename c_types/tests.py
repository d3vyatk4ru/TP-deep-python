import unittest
import time
from mult_matrix import matrix_generate, mat_mult_seq_c, mat_mult_seq_py


class TestMultiplyMatrix(unittest.TestCase):

    def test_correct_mult_py(self):

        matrixes = tuple([
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ])

        result = mat_mult_seq_py(matrixes)

        self.assertListEqual(result, [[19, 22], [43, 50]])

    def test_correct_mult_c(self):

        matrixes = tuple([
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ])

        result = mat_mult_seq_c(matrixes, 2, 2)

        self.assertListEqual(result, [[19, 22], [43, 50]])

    def test_speed_c_and_py(self):

        size = 50

        matrixes = matrix_generate(100, size)

        start = time.time()

        mat_mult_seq_py(matrixes)

        py_time = time.time() - start

        start = time.time()

        mat_mult_seq_c(matrixes, len(matrixes), size)

        c_time = time.time() - start

        self.assertTrue(c_time < py_time)


if __name__ == '__main__':

    unittest.main()
