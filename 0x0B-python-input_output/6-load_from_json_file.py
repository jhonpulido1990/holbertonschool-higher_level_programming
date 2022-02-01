#!/usr/bin/python3
'''
Write a function that creates an
Object from a “JSON file”:
You must use the with statement
'''
import json


def load_from_json_file(filename):
    '''You must use the
    with statement
    '''
    with open(filename) as f:
        return json.load(f)
