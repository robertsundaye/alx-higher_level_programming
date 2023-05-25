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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get/Set returns and check the width for exactness
        """
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get/Set returns and check the height for exactness
        """
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
