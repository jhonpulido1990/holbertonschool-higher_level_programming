#!/usr/bin/python3
'''function that prints a square with the character #
the way to use it is as follows
print_square(2): expectation
    ##
    ##'''


def print_square(size):
    '''functions that evaluate
    if the size variable is a
    positive integer'''
    if isinstance(size, float) < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                print("{}".format('#' * size))
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
