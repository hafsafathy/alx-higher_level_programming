#!/usr/bin/python3
"""Write a class Student that defines a student by: (based on 10-student.py)
"""


class Student:
    """ Class"""

    def __init__(self, first_name, last_name, age):
        """initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns directory description """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        Represents of Student into json format

        Attributes:
            attrs (dict): A python object to convert

        Return:
            Student class as a json format
        """
        for key, value in json.items():
            setattr(self, key, value)
