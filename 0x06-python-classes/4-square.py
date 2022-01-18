#!/usr/bin/python3
'''create class'''


class Square:
    '''create definition'''
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        return self.__size ** 2
