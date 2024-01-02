#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """My first attempt of inheritance
    This class inherits from the list class"""
    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = sorted(self[:])
        print(sorted_list)
        return sorted_list
