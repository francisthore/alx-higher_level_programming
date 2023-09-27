#!/usr/bin/python3

import string

print(string.ascii_uppercase.translate(str.maketrans('', '', '\x00')), end='\n')
