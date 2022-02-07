#!/usr/bin/python3
"""
Program that votes 4096 times for my id.
"""
import requests


url = 'http://158.69.76.135/level1.php'

with requests.session() as session:
    for i in range(4096):
        res = session.get(url)
        value = res.cookies['HoldTheDoor']

        params = {
            "id": "3779",
            "holdthedoor": "submit",
            "key": value
        }
        votes = session.post(url, data=params)
    print(votes.text)
    print(votes.status_code)

