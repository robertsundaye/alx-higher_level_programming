#!/usr/bin/python3
for letters in range(97, 123):
    print("{}".format(chr(letters)), end="")
    if (letters == 101 | letters == 113):
        continue
