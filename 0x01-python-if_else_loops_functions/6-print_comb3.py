#!/usr/bin/python3

res = ""
for i in range(10):
    for j in range(i + 1, 10):
       res += "{:d}{:d}, ".format(i, j)
print(res.rstrip(', '))
