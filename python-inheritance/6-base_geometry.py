#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an area method"""


class BaseGeometry:
    """Represents a base geometry object"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
