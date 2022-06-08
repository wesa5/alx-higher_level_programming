#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return new_matrix
