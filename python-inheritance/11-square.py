#!/usr/bin/python3
"""Module that defines a class Square with its own string representation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new Square

        Args:
            size: the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is not greater than 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
