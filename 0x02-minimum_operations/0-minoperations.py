#!/usr/bin/python3
"""Calculates minimum number of copy/paste operations
to get n H characters
"""

import math


def minOperations(n):
    """Computes minimum copy/paste operations for n chars

    Args:
        n (int): Number of H characters to create

    Returns:
        int: Minimum number of copy/paste operations
    """

    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
