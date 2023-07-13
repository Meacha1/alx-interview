#!/usr/bin/python3

"""
This module contains a function minOperations that calculates the fewest number
of operations needed to achieve exactly n H characters in a file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve exactly n H
    characters in a file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.

    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n /= divisor
        else:
            divisor += 1

    return operations
