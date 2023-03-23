#!/usr/bin/python3

"""The concept tests a triangular array of binomial coefficients, where each element of the triangle is the sum of the two elements directly above it also referred to as Pascal's Triangle 
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n
    

    Args:
        n (int): Size of the Pascal's triangle
    """
    lst = []
    if (n <= 0):
        return lst
    else:
        for i in range(n+1):
            tmp = []
            # first element is always 1 
            elem = 1
            for j in range(1, i+1):

# first value in the line is always 1 
                tmp.append(elem)
                # using Binomial Coeff

                elem = elem * (i - j) // j
        if (len(tmp)):
            lst.append(tmp)

    return lst

