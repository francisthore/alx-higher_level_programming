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

        try:
            self.__size = size
        except Exception as e:
            print(e)
            
