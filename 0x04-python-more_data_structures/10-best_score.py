#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    new_dictionary = sorted(a_dictionary)
    return new_dictionary[-1]
