#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """not allowed to import any module"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
