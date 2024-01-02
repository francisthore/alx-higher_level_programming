#!/usr/bin/python3
"""This module returns a list of available
attributes and methods of an object"""


def lookup(obj):
    """returns list of available attributes and methods"""
    return dir(obj)
