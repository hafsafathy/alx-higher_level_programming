#!/usr/bin/python3
"""function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends to the end of a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
