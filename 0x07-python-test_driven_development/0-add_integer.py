#!/usr/bin/python3

"""This a module that adds integers
    It qualifys the values and casts them into ints
    I am also running tests
    I am just putting lines rn idk what to write
"""


def add_integer(a, b=98):
    """This function adds two integers
        Returns sum of the two integers
    """
    if (a in None or (type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")

    if (b is None or (type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
