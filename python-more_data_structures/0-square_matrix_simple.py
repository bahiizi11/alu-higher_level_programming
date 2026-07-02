#!/usr/bin/python3
"""Module that squares all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix

    Args:
        matrix: a 2 dimensional array

    Returns:
        A new matrix, same size, with squared values
    """
    return [[value ** 2 for value in row] for row in matrix]
