#!/usr/bin/python3
"""
The concept tests a triangular array of binomial coefficient"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n.
    parameters:
        n [int]:
            the number of rows
    return:
        [list of lists of ints]:
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    matrix = []
    if n <= 0:
        return matrix
    for i in range(n):
        arr = []
        for j in range(i + 1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                arr.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        matrix.append(arr)
    return matrix
