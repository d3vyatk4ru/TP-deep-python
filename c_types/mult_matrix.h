#ifndef _MULT_MATRIX_H
#define _MULT_MATRIX_H

#ifdef __cplusplus
extern ("C") {
#endif

#include <stdlib.h>

void multiply_c(int **left, int **right, int **result, int size);

int **mat_mult_seq_c(int ***matrix_sequence, int **result, int seq_size, int size);

void copy(int **left,int **right, int size);

#ifdef __cplusplus
}
#endif

#endif // _MULT_MATRIX_H