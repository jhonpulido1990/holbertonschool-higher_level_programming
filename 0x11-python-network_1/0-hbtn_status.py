#!/usr/bin/python3
"""Write a Python script that fetches
https://intranet.hbtn.io/status"""
from urllib.request import urlopen
import json

if __name__ == "__main__":
    print("Body response:")
    with urlopen('https://intranet.hbtn.io/status') as response:
        info = response.read()
        print('\t' + '- type: {}'.format(type(info)))
        print('\t' + '- content: ' + str(info))
        print('\t' + '- utf8 content: ' + info.decode("utf-8"))
