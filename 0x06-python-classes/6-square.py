#!/usr/bin/python3
'''create class'''


class Square:
    '''create definition'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if (value[0] < 0 and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (type(value[0]) != int and type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))
