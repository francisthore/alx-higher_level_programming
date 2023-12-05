#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            print("{}".format(my_list[i]), sep="", end="")
            n += 1
        print()
        return n
    except Exception as e:
        print()
        return n
