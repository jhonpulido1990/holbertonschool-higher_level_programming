#!/usr/bin/python3
'''

Write the class Square that inherits from Rectangle:



'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class Square inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        attr = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                if hasattr(self, attr[i]):
                    setattr(self, attr[i], args[i])
        if kwargs:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        dictio = {}
        dictio.update(id=self.id, size=self.size, x=self.x, y=self.y)
        return dictio
