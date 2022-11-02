#!/usr/bin/python3
"""This is a base module containing a base class"""


class Base:
    """Base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructing the necessary attributes for the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
