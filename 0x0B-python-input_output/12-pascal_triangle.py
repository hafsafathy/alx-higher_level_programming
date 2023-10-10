#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascals triangle of n
"""


def pascal_triangle(n):
    """fun
    """
    if n <= 0:
        return []

    angle = [[1]]
    while len(angle) != n:
        t = angle[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        angle.append(tmp)
    return angle
