#!/usr/bin/python3

def uppercase(str):
    res = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            upper_letter = chr(ord(letter) - 32)
            res += "{}".format(upper_letter)
        else:
            res += "{}".format(letter)
    print("{}".format(res))
