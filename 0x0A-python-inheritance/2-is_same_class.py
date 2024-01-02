#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance of class"""
    if a_class != object and isinstance(obj, a_class):
        return True
    return False
