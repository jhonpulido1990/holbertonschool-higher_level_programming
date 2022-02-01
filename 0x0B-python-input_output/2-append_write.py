#!/usr/bin/python3
'''Write a function that
appends a string at the end of a
text file (UTF8) and returns the
number of characters added:
'''


def append_write(filename="", text=""):
    '''
    Write a function that appends a string
    at the end of a text file'''
    with open(filename, 'a') as f:
        fcount = f.write(text)
    f.close()
    return fcount
