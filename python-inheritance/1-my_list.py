#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list"""


class MyList(list):
    """Represents a list that can print itself sorted"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
