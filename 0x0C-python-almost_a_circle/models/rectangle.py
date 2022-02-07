#!/usr/bin/python3
'''Create a folder named models with an
empty file __init__.py inside - with this
file, the folder will become a Python package
'''
from models.base import Base


class Rectangle(Base):
    '''
    define of subclass rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        define of constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        property definition width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        method that sets the value of a property width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        property definition height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        method that sets the value of a property height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        property definition x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        method that sets the value of a property x
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        property definition y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        method that sets the value of a property y
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        size area
        '''
        return self.__width * self.__height

    def display(self):
        '''
        funtion display
        '''
        rect = ""
        rect = "\n" * self.y
        for i in range(self.height):
            rect += ' ' * self.x + '#' * self.width
            if i < (self.height - 1):
                rect += '\n'
        print(rect)

    def __str__(self):
        '''
        print date
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''
        data update
        '''
        attr = ["id", "width", "height", "x", "y"]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for i in range(len(args)):
            if hasattr(self, attr[i]):
                setattr(self, attr[i], args[i])

    def to_dictionary(self):
        '''
        create dictionary
        '''
        dic = {}
        dic.update(x=self.__x, y=self.__y, id=self.id,
                   height=self.__height, width=self.__width)
        return dic
