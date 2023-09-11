#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = my_list[:]
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
