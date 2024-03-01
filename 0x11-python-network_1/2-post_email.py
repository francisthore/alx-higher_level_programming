#!/usr/bin/python3
""" Sends a post request to
a server
"""

if __name__ == "__main__":
    import urllib
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email' : email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read()
    print(body.decode('utf-8'))    
