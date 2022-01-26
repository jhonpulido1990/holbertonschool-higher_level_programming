#!/usr/bin/python3
'''This function allows 
you to add two integers or floats and its 
result is an integer.
add_integer(1, 3)
4 '''


def add_integer(a, b=98):
    '''in this function it is evaluated
    if the variables are 
    integers, floats'''
    if not isinstance(a, (int, float)) and a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) and b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
