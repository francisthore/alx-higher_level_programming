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
    new_line = False
    for letter in text:
        if new_line:
            if letter == " ":
                continue
            new_line = False
        if letter in my_chars:
            print(letter)
            print("")
            new_line = True
        else:
            print(letter, end="")
