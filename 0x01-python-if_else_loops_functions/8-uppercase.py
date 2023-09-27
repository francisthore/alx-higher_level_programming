#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            upper_letter = chr(ord(letter) - 32)
            print(upper_letter, end='')
        else:
            print(letter, end='')
    print()
