#!/usr/bin/python3
"""Module that defines a rectangle"""



class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Constructing the necessary attributes."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        :return: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        :param value: The value of the set width.

        :raises TypeError: width must be an integer.
        :raises ValueError: width must be >+ 0

        :return: int
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Retrieves the height of the rectangle
        :return: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        :param value: The value of the set height.

        :raises TypeError: height must be an integer.
        :raises ValueError: height must be >+ 0

        :return: int
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

