#!/usr/bin/python3
for letter in map(chr, range(97, 123)):
    if letter == 'q' or letter == 'e':
        continue
    print("{}".format(letter), end="")
