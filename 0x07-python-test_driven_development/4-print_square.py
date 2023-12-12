#!/usr/bin/python3

"""Prints a square using # signs
    Has 1 function that handles everything
    tests will be written separately
    Lets goooo
"""


def print_square(size):
    """Prints a square using #
        tests separated
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
