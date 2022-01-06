#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()
    for i in copy_dict.keys():
        if value == copy_dict.get(i):
            a_dictionary.pop(i, None)
    return a_dictionary
