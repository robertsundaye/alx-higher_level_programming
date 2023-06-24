#!/usr/bin/python3

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

        @property
        def mag(self):
            return (((self.x ** 2) + (self.y ** 2)) ** (1/2))

        def reset(self):
            self.move(0,0)

        def move(self, newx, newy):
            self.x = newx
            self.y = newy

        def movex(self, newx):
            self.x = newx

        def movey(self, newy):
            self.y = newy

        @property
        def showpoint(self):
            return f"({self.x},{self.y})"

        def __repr__(self):
            return f"{self.showpoint()}"

from random import randint

point1 = Point(6,7)
print(point1.showpoint)

