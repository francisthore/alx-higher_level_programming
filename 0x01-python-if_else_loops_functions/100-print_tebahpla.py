#!/usr/bin/python3
res = ""
for char in "zYxWvUtSrQpOnMlKjIhGfEdCbA":
    if char.isupper():
        res += "{}".format(char)
    else:
        res += "{}".format(char.lower())

print("{}".format(res), end='')
