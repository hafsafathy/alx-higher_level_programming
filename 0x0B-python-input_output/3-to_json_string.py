#!/usr/bin/python3
"""function that returns the JSON
representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """function

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
