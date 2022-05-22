from typing import List, Tuple
import ctypes
import time
import random
import os

SIZE = 70


def multiply_py(left: List[List[int]],
                right: List[List[int]],
                size: int) -> List[List[int]]:
    """ Multiply ONLY square matrix """

    result: List[List[int]] = [
        [0 for _ in range(size)] for _ in range(size)
    ]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += left[i][k] * right[k][j]

    return result


def mat_mult_seq_py(matrix_sequence: Tuple[List[List[int]]])\
                    -> List[List[int]]:
    """ Multiply sequence of matrix """

    size: int = len(matrix_sequence[0])

    result: List[List[int]] = [
        [0 for _ in range(size)] for _ in range(size)
    ]

    result = matrix_sequence[0]

    for idx in range(len(matrix_sequence) - 1):
        result = multiply_py(result, matrix_sequence[idx + 1], size)

    return result


def mat_mult_seq_c(matrix_sequence: Tuple[List[List[int]]],
                   n_matrix: int,
                   size: int) -> List[List[int]]:
    """" ABC """

    matrixes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_int)) * n_matrix)()

    for i in range(n_matrix):
        matrixes[i] = (ctypes.POINTER(ctypes.c_int) * size)()
        for j in range(size):

            matrixes[i][j] = (ctypes.c_int * size)()

            for k in range(size):
                matrixes[i][j][k] = matrix_sequence[i][j][k]

    output = (ctypes.POINTER(ctypes.c_int) * size)()

    for i in range(size):
        output[i] = (ctypes.c_int * size)()

    lib = ctypes.cdll.LoadLibrary(os.path.abspath('libmatmul.so'))

    mat_mult = lib.mat_mult_seq_c

    mat_mult(ctypes.byref(matrixes), output, n_matrix, size)

    matrix_output = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(output[i][j])
        matrix_output.append(row)

    return matrix_output


def matrix_generate(n_matrix: int = 2,
                    size: int = 2):

    if n_matrix < 1:
        raise Exception('Number of matrix  < 1')

    matrixes = []

    for _ in range(n_matrix):
        mat = []
        for _ in range(size):
            col = []
            for _ in range(size):
                col.append(random.randint(-10, 10))
            mat.append(col)
        matrixes.append(mat)

    return matrixes


if __name__ == '__main__':

    matrix = matrix_generate(100, SIZE)

    start = time.time()

    mat_mult_seq_py(matrix)

    print(f'Time of Python code: {time.time() - start}')

    start = time.time()

    mat_mult_seq_c(matrix, len(matrix), SIZE)

    print(f'Time of C code: {time.time() - start}')
