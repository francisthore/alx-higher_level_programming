#!/usr/bin/python3

for char in "zYxWvUtSrQpOnMlKjIhGfEdCbA":
    if char.isupper():
        print(char, end='')
    else:
        print(char.lower(), end='')
