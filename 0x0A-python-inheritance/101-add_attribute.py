#!/usr/bin/python3
""" function that adds a new attribute to
an object if it’s possible"""


def add_attribute(obj, name, value):
    """ not allowed to use try/except"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
