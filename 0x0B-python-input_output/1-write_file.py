#!/usr/bin/python3
'''
Write a function that writes a string to
a text file (UTF8) and returns the number
of characters written:
'''


def write_file(filename="", text=""):
    '''
    Write a function that writes a
    string to a text file (UTF8)'''
    with open(filename, 'w', encoding="utf_8") as f:
        fcount = f.write(text)
    f.close()
    return fcount
