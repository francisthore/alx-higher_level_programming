#!/usr/bin/python3
""" Sends a request using the
requests module and prints error code
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    request = requests.get(url)
    stat_code = request.status_code

    if stat_code >= 400:
        print('Error code: {}'.format(stat_code))
    else:
        print(request.text)
