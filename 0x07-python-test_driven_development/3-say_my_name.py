#!/usr/bin/python3

"""This module prints a user's full name
    It has two parameters
    First name is mandatory and last name is optional
    Let us code it
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <firstname> <lastname>
        Returns the name string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
