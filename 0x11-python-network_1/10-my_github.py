#!/usr/bin/python3
"""
Write a Python script that fetches
https://intranet.hbtn.io/status
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    param = {'search': argv[1]}
    r = requests.get(url, params=param)

    matching_ppl = r.json()
    print("Number of results: {}".format(matching_ppl.get('count')))
    for person in matching_ppl.get('results'):
        print(person.get('name'))
