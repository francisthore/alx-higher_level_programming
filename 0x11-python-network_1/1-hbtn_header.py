#!/usr/bin/python3
""" Gets the value of a header
from a response
"""
import urllib
import os
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
