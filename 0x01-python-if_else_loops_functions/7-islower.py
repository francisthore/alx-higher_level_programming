#!/usr/bin/python3
def islower(c):
    if c in map(chr, range(ord('a'), ord('z')+1)):
        return True
    return False
