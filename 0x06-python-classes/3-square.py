#!/usr/bin/python3
"""
This is a module that defines an squares
"""


class Square:
    """This is a class that defines a square"""

    def __init__(self, size=0):
        """This is a function that initializes a sqaure object

        Args:
            self: the object itself
            size: size of one side of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """
            Calculates the area of a square
        """
        return self.__size ** 2
