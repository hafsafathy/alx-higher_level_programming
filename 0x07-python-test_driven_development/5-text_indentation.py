#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """ function that prints a text with 2 new lines
        after each of these characters: ., ? and :

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for m in ".?:":

        text = (m + "\n\n").join(
            [line.strip(" ") for line in text.split(m)])

    print(text, end="")
