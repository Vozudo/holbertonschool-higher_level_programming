#!/usr/bin/python3
"""Module that contains "Base" class"""


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