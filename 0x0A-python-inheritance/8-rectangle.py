#!/usr/bin/python3
'''
Write a class BaseGeometry (based on 6-base_geometry.py).
Public instance method: def area(self): that raises an
Exception with the message area() is not implemented
'''


class BaseGeometry:
    '''
    Write a class BaseGeometry
    (based on 6-base_geometry.py)'''
    def __init__(self, width, height):
        self.__width = width
        self.__heigth = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(self.__width) is int and self.__width > 0:
            pass
        if type(self.__heigth) is int and self.__heigth > 0:
            pass
