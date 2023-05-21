#!/usr/bin/python3
""" Defining a class Rectangle """

class Rectangle:
    """ the class itself """
    def __init__(self, width=0, height=0):
        """
        initiation function of the class
        :parameters: width and height and self
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        the getter function that receive and return the width and height inputs.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        setter function.
        :Args: value and self
        """
        if value is not int:
            raise TypeError("width must be na integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        getter fuction for height that returns the height input
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        setter functions of height
        """
        if value is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
