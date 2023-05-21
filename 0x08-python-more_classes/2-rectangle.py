#!/usr/bin/python3
""" Defining a class Rectangle """

class Rectangle:
    """ the class itself """

    def __init__(self, width=0, height=0):
        """initializing a new class

        Args:
             width(int): the width of the class
             height(int): the height of the class
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Get/Set returns and check the width for exactness
        """
        return self._width

    @width.setter                                                                                                                                def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get/Set returns and check the height for exactness
        """
        return self._height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ return the area of the rectangle """
        area = self._width * self._height
        return area

    def perimeter(self):
        """ returns the parameter of the ractangle """
        if self._width == 0 or self._height == 0:
            param = 0
            return param
        else:
            param = 2 * (self._width + self._height)
            return param


