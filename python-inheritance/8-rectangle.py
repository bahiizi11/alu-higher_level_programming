#!/usr/bin/python3
"""Module that defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a new Rectangle

        Args:
            width: the width of the rectangle
            height: the height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is not greater than 0
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
