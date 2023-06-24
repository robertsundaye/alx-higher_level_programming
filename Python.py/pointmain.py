#!/usr/bin/python3
from Point import Point
from random import randint

list1 = [Point(randint(-10,10), randint(-10,10)) for _ in range(5)]
list2 = [Point(randint(-5,5), randint(-5,5)) for _ in range(5)]

for p in list1:
    print(p.showpoint())
print("-------------------------")
for p in list2:
    print(p.showpoint())
