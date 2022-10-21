#!/usr/bin/python3
"""Module that contains "Base" class"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string of list_objs to a file"""
        obj_list = []
        if list_objs is not None:
            for item in list_objs:
                obj_list.append(item.to_dictionary())

        filename = str(cls.__name__) + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(obj_list))
