#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """a function that reads and prints contents of
    a file to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
