#!/usr/bin/python3
'''Returns a list of lists of integers representing the Pascal's triangle'''

def pascal_triangle(n):
    '''Returns a list of lists of integers representing the Pascal's triangle'''
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n-1)
        new_row = [1]
        for i in range(len(triangle[-1])-1):
            new_row.append(triangle[-1][i] + triangle[-1][i+1])
        new_row.append(1)
        triangle.append(new_row)
        return triangle
    