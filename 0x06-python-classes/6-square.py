#!/usr/bin/python3
'''create class'''


class Square:
    '''create definition'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (value[0] <= 0 and value[1] <= 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (value is None or value[0] is None or value[1] is None):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        x = 0
        z = 0
        while(z < self.__position[1]):
            print()
            z += 1
        if (self.__size == 0):
            print()
        while(x < self.__size):
            y = 0
            print(" " * self.__position[0], end='')
            while(y < self.__size):
                print("#", end='')
                y += 1
            print()
            x += 1
