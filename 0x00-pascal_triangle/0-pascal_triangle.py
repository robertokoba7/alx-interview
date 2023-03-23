#!/usr/bin/python3

"""The concept tests a triangular array of binomial coefficients, where each element of the triangle is the sum of the two elements directly above it also referred to as Pascal's Triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n
    """

    my_list = []
    if (n <= 0):
        return my_list
    my_list.append([1])
    for i in range(n - 1):
        my_list.append([1] + [my_list[i][a] + my_list[i][a + 1]
                              for a in range(len(my_list[i]) - 1)] + [1])
        return my_list
