#!/usr/bin/python3
"""Write a class Student that defines a student by
"""


class Student:
    """ Class"""

    def __init__(self, first_name, last_name, age):
        """initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns directory description """
        return self.__dict__.copy()
