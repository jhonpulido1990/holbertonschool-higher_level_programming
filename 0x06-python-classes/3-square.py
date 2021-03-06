#!/usr/bin/python3
'''create class'''


class Square:
    '''create initializacion'''
    def __init__(self, size=0):
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
