#!/usr/bin/python3
"""
Sends a post request
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    request = requests.post(url, data)

    print(request.text)
