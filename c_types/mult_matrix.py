from typing import List, Tuple
import ctypes
import time
import random

SIZE = 3

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


def mat_mult_seq_py(matrix_sequence: Tuple[List[List[int]]]) -> List[List[int]]:
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
                    n_matrix: int):
    """" ABC """

    matrixes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_int)) * n_matrix)()

    for i in range(n_matrix):
        matrixes[i] = (ctypes.POINTER(ctypes.c_int) * SIZE)()
        for j in range(SIZE):

            matrixes[i][j] = (ctypes.c_int * SIZE)()

            for k in range(SIZE):
                matrixes[i][j][k] = matrix_sequence[i][j][k]

    output = (ctypes.POINTER(ctypes.c_int) * SIZE)()

    for i in range(SIZE):
        output[i] = (ctypes.c_int * SIZE)()

    lib = ctypes.cdll.LoadLibrary('/home/d3vyatk4ru/Рабочий стол/c_ext/libmatmul.so')

    mat_mult = lib.mat_mult_seq_c

    mat_mult(ctypes.byref(matrixes), output, n_matrix, SIZE)

    for i in range(SIZE):
        for j in range(SIZE):
            print(output[i][j], end=' ')
        print()

def matrix_generate(n_matrix: int):
    pass


if __name__ == '__main__':

    matrixes = tuple([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 0], [1, 2]],
        [[3, 4], [5, 6]],
        [[7, 8], [9, 0]],
    ])

    start = time.time()

    print(mat_mult_seq_py(matrixes))

    print(f'Time of Python code: {time.time() - start}')

    start = time.time()

    mat_mult_seq_c(matrixes, len(matrixes))

    print(f'Time of C code: {time.time() - start}')
