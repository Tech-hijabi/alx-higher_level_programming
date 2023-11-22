#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a class square."""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
