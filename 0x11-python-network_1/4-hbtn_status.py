#!/usr/bin/python3
""" Sends a request using the
requests module
"""

if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    request = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(request.text)))
    print('\t- content: {}'.format(request.text))
