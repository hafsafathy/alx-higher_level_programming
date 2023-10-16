#!/usr/bin/python3
""" function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """

    numline = []
    with open(filename, 'r', encoding="utf-8") as f:
        for ln in f:
            numline += [ln]
            if ln.find(search_string) != -1:
                numline += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(numline))
