#!/usr/bin/python3
""" Defining a class Rectangle """

class Rectangle:
    """ the class itself """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if self._width not int:
            raise TypeError("width must be na integer")
        if self._width < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if _height not int:
            raise TypeError("height must be an integer")
        if _height < 0:
            raise ValueError("height must be >= 0")
        self._height = value

