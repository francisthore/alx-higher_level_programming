#!/usr/bin/python3
"""
Gets header from response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    request = requests.get(url)
    header = 'X-Request-Id'
    print(request.headers.get(header, 'Header not found'))
