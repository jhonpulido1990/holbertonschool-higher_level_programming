#!/usr/bin/python3
'''
Write a class BaseGeometry (based on 6-base_geometry.py).
Public instance method: def area(self): that raises an
Exception with the message area() is not implemented
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Write a class BaseGeometry
    (based on 6-base_geometry.py)'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
