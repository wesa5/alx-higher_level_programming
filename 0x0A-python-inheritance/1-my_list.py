#!/usr/bin/python3
"""Contains `MyList` class"""


class MyList(list):
    """Class that extends the list base class"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
