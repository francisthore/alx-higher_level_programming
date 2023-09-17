#!/usr/bin/python3


def best_score(a_dictionary):
    best_mark = 0
    best_student = ""
    if not a_dictionary:
        return
    for key, value in a_dictionary.items():
        if value > best_mark:
            best_mark = value
            best_student = key
    return best_student
