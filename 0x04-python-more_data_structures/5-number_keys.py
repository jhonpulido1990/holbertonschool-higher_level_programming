#!/usr/bin/python3
def number_keys(a_dictionary):
    for i in a_dictionary:
        if i != str:
            return a_dictionary.get('number')
