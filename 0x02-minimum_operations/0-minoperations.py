#!/usr/bin/python3
"""
This is a 2 key keyboard problem.
"""


def minOperations(n):
    """
    Given:
        Current number: n
        Returns: minimum number of operations
                Otherwise 0, if impossible to generate n H char
    """
    # Initialize the variables current, count, buffer1 to run dynamic
    current = 1
    count = 0
    buffer1 = 0
    # when current is less than n we return the remaining number of times H.
    while current < n:
        rest = n - current

        # Check if we can generate a sequence of H char
        if(rest % current == 0):
            buffer1 = current
            current += buffer1
            count += 2

        else:
            current += buffer1
            count += 1

    # Otherwise, return minimum number of operations
    if current == n:
        return count
    else:
        return 0
