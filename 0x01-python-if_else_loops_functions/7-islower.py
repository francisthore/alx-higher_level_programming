#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError()
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False
