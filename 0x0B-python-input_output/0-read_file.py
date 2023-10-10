#!/usr/bin/python3
"""function that reads a text file
and print it to stdout
"""


def read_file(filename=""):
    """ Function that reads a text file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        x = f.read()
        print(x, end='')
