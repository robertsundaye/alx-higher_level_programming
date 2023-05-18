#!/usr/bin/python3

from Question1 import User

question_list = [
    "1. Find the equation of the line passing through the points: (0,1) and (2,4)\n(a) 2x-3y=-2\n(b) 3x-2y=2\n(c) 3x-3y=-2\n(d) 3x-2y=-2\n",
    "2. State the gradient and the intercept on the y-axis of the following lines:  2x – y = 3\n(a) m=2,y=-3\n(b) m=6,y=2\n(c) m=6,y=1\n(d) m=5,y=3\n",
    "3. Find the mid-point of the line passing through the following pairs of points: (4,2) and (2,5)\n(a) M=7/2,3\n(b) M=3,7/2\n(c) M=4,6\n(d) M=7,3\n",
    "4 .Find the length of the lines passing through the following pairs of points: (4,2) and (2,5)\n(a) L=sqrt 13\n(b) L=sqrt 12\n(c) L=sqrt 3\n(d) L=sqrt 10\n",
    "5. Find the slope of the lines passing through the following pairs of points: (1,4) and (3,2)\n(a) m=7\n(b) m=5\n(c) m=-1\n(d) m=1\n\n",
    "6. Find the equation of the line which passing through the point (3,-2) and is parallel to 5x – y + 3 = 0\n(a) 5x-y=5\n(b) 5x-y=7\n(c) 5x-y=17\n(d) 5x-y=18\n"
]

question = [
    User(question_list[0], "d"),
    User(question_list[1], "a"),
    User(question_list[2], "b"),
    User(question_list[3], "a"),
    User(question_list[4], "c"),
    User(question_list[5], "c")
]

def run(question):
    infor = input("\nEnter your: ").rstrip().upper()
    level = input("\nWhat is your class: ").rstrip().upper()
    input("\nThis is God subject digital test by Robert Sundaye. Wish you the best of luck scholar\nHit the enter key to start test\n")
    score = 0
    for question in question:
        answer = input(f"{question.prompt}\n")
        if answer == question.answer:
            score += 10
    print("Your final grade is " + str(score) + "/60")
    with open("grade.txt", "a") as file:
        file.write(f"{infor} , Grade: {level}, {score}\n")

run(question)
