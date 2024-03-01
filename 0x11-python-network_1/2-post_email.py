#!/usr/bin/python3
""" Sends a post request to
a server
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib import parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = parse.urlencode(values)
    data = data.encode('ascii')
    request = Request(url, data)
    with urlopen(request) as response:
        body = response.read()
    print(body.decode('utf-8'))
