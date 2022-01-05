#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    transposed = []
    for i in range(len(matrix)):
        transposed_row = []
        for j in range(len(matrix[i])):
            transposed_row.append(matrix[i][j] * matrix[i][j])
        transposed.append(transposed_row)
    return transposed
