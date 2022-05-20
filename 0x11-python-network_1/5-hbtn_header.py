#!/usr/bin/python3
"""
Write a Python script that fetches
https://intranet.hbtn.io/status
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
