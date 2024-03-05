#!/usr/bin/python3
"""
Sends some data via post as an api
"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) != 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'

    request = requests.post(url, data={'q': letter})
    try:
        response = request.json()

        if response:
            print('[{}] {}'.format(response['id'], response['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
