#!/usr/bin/python3
"""Module that defines a function to build Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's Triangle

    Args:
        n: the number of rows of the triangle

    Returns:
        A list of lists representing the triangle, or an empty list
        if n is less than or equal to 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
