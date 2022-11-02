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
        """
        Sets the width of the rectangle.

         Raises:
              TypeError - if the width is not an integer.
              ValueError - if the width is under 0 or equals 0

        """
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Raises:
              TypeError - if the height is not an integer.
              ValueError - if the height is under 0 or equals 0
        """

        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")

    @property
    def x(self):
        """Retrieves the value x"""
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the value x.

         Raises:
              TypeError - if x is not an integer.
              ValueError - if x is under 0 or equals 0

        """
        self.__x = x
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Retrieves the value y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the value y.

         Raises:
              TypeError - if y is not an integer.
              ValueError - if y is under 0 or equals 0

        """
        self.__y = y
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")

