#!/usr/bin/python3


from logging import exception


class Square:
    def __init__(self, size=0):
            self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        if(type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
