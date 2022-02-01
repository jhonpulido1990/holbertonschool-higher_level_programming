#!/usr/bin/python3
'''
Write a function that reads a text file
(UTF8) and prints it to stdout:

'''


def read_file(filename=""):
    '''Write a function that reads a
    text file (UTF8) and prints it
    to stdout:'''
    with open(filename, encoding='utf_8') as f:
        data_read = f.read()
        stdout = data_read
        print(stdout)
    f.close()
