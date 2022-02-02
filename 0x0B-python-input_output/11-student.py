#!/usr/bin/python3
'''
Write a class Student that

defines a student by:
'''


class Student:
    '''Write a class Student
    that defines a student by:
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        for key, valor in json.items():
            setattr(self, key, valor)
