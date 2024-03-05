#!/usr/bin/python3
""" Gets the value of a header
from a response

Usage: ./1-hbtn_header.py <URL>
"""

if __name__ == "__main__":
    import urllib
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(urllib.request.Request(url)) as response:
        print(dict(response.headers).get("X-Request-Id"))
