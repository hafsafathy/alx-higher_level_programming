#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """ function that adds 2 integers

    Args:
        a: first num
        b: second num

    Returns:
        The addition of a and b

    Raises:
        TypeError: If a or b arenot integer

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
