#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Initialize

        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        calculates the area of the Square
        """
        return self.__size ** 2
