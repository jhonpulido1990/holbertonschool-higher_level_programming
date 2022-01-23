#!/usr/bin/python3
'''create class'''


def print_square(size):
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
