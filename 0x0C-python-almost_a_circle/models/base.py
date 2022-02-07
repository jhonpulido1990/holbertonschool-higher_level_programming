#!/usr/bin/python3
'''Write the first class Base:
Create a folder named models with
an empty file __init__.py inside -
with this file, the folder will become
a Python package'''
import json


class Base:
    '''
    Create a file named models/base.py
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        namefile = "{}.json".format(cls.__name__)
        lista = []
        if list_objs is not None:
            for i in list_objs:
                lista.append(cls.to_dictionary(i))
        with open(namefile, 'w') as f:
            f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        listing = []
        namefile = "{}.json".format(cls.__name__)
        try:
            with open(namefile, 'r') as f:
                diction = cls.from_json_string(f.read())
            for instance in diction:
                listing.append(cls.create(**instance))
            return listing
        except FileNotFoundError:
            pass
