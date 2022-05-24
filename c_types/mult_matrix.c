#include "mult_matrix.h"

void copy(int **left,int **right, int size) {
    for (int i = 0; i <  size; ++i) {
        for (int j = 0; j <  size; ++j) {
            right[i][j] = left[i][j];
        }
    }
}

void multiply_c(int **left, int **right, int **result, int size) {

    for(int i = 0; i < size; i++) {
        
        for(int j = 0; j < size; j++) {

            result[i][j] = 0;

            for(int k = 0; k < size; k++) {
                result[i][j] += left[i][k] * right[k][j];
            }
        }
    }
}

int **mat_mult_seq_c(int ***matrix_sequence, int **result, int seq_size, int size) {

    int **tmp = (int **) malloc(size * sizeof(int*));
    for (int i = 0; i < size; ++i) {
        tmp[i] = (int *) malloc(size * sizeof(int));
    }

    copy(matrix_sequence[0], tmp, size);

    for (int i = 0; i < seq_size - 1; ++i) {
        multiply_c(tmp, matrix_sequence[i + 1], result, size);

        copy(result, tmp, size);
    }

    for (int i = 0; i < size; ++i) {
        free(tmp[i]);
    }

    free(tmp);

    return result;

}
