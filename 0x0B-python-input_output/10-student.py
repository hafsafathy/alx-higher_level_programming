#!/usr/bin/python3
"""Write a class Student that defines a student by: (based on 9-student.py)
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
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            newlist = {}

            for i in range(len(attrs)):
                for h in obj:
                    if attrs[i] == h:
                        newlist[h] = obj[h]
            return newlist

        return obj
