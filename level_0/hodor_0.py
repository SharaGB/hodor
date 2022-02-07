#!/usr/bin/python3
"""
Program that votes 1024 times for my id.
"""
import requests


url = 'http://158.69.76.135/level0.php'

with requests.session() as session:
    res = session.get(url)

    params = {
        "id": "3779",
        "holdthedoor": "submit"
    }

    for i in range(1024):
        votes = session.post(url, data=params)
    print(votes.text)
    print(votes.status_code)
