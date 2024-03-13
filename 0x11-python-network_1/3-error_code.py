#!/usr/bin/python3
""" Error handling with urllib
package
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    try:
        with urlopen(Request(url)) as response:
            body = response.read()
        print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
