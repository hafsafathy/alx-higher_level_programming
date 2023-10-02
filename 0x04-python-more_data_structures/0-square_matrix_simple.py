#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_max = matrix.copy()

    for i in range(len(matrix)):
        new_max[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_max)
