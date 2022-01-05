#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        new_dictionary = max(a_dictionary)
        return new_dictionary
