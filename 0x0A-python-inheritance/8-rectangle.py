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
