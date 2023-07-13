#!/usr/bin/python3
"""Calculates minimum number of copy/paste operations 
to get n H characters"""

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
    
    for i in range(int(math.sqrt(n)) + 1, 0, -1):
        if n % i == 0:
            return i + minOperations(int(n / i))

    return minOperations(n - 1) + 1
