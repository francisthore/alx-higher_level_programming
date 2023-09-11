#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    i = length - 1
    idx = i - length

    for elem in my_list:
        print("{:d}".format(my_list[idx]))
        i -= 1
        idx = i - length
