#!/usr/bin/python3
"""function for Pasacls triangle"""


def pascal_triangle(n):
    """
    returns list of ints
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        triangle.append(current)
    return triangle
