#!/usr/bin/python3

"""This module prints a texts with two new lines
    upon occurance of . ? or :
    tests will be written
    Lets goooo
"""


def text_indentation(text):
    """This function prints a text with 2 new lines 
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    my_chars = ('.', '?', ':')
    for letter in text:
        print("{}".format(letter).lstrip(), end="")
        if letter in my_chars:
            print("")
            print("")
