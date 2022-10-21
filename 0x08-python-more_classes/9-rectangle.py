#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

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

        :return:         """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        The area of the rectangle, returns the calculated area of the rectangle.

        :return: int
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        The perimeter of the rectangle, returns the calculated perimeter of the rectangle.

        :return: int
        """

        if self.__width == 0 and self.__height == 0:
            return 0

        return 2 * self.__width + 2 * self.__height

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of an object. Returns a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)


