#!/usr/bin/python3
"""This module represents a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle that inherits a Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructing the necessary attributes of the class"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        self.__width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle"""
        self.__height = height

    @property
    def x(self):
        """Retrieves the value x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the value x"""
        self.__x = x

    @property
    def y(self):
        """Retrieves the value y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the value y"""
        self.__y = y
