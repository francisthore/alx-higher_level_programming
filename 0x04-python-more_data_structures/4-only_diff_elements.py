#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_elems = [item for item in set_1 | set_2]
    return diff_elems
