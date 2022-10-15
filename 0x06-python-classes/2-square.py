#!/usr/bin/python3
# 2-square.py by Bennet Ukoh
"""Defines a square"""



class Square:
    """
    The class defines a square.

    Attribute:
      size (int): Takes the size of the square.
    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the Square object.

        param size: size of the Square.

        raise  TypeError: size must be an integer.
        raise  ValueError: size must be >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


