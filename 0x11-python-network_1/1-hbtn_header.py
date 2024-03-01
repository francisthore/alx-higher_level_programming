#!/usr/bin/python3
""" Gets the value of a header
from a response
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    import sys

    url = sys.argv[1]
    with urlopen(Request(url)) as response:
        result = response.getheader('X-Request-Id')
    if result:
        print(result)
