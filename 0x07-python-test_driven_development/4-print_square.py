#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """function that prints a square with the character #.

    Args:
        size: The int size.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")
