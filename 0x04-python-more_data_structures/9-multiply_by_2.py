#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    doubled = {}
    keys = list(a_dictionary)

    for key in keys:
        doubled[key] = a_dictionary[key] * 2
    return doubled
