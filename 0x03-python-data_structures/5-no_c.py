#!/usr/bin/python3
def no_c(my_string):
    character = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            character += i
    return character
