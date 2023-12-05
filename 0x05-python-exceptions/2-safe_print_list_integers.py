#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                n += 1
            except Exception as e:
                pass
        print()
        return n
    except IndexError as e:
        print(e)
        return n
    except Exception as e:
        print(e)
