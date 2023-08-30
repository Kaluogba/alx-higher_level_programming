#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square Class.

This module defines the Square class, which represents a square shape.

Example:
    To create a square object:
    square = Square()

Attributes:
    None

Todo:
    * Implement methods for calculating area and perimeter.

"""

class Square:
    """Represents a square shape.

    A square is defined by its side length. The class provides methods for
    calculating the area and perimeter of the square.

    Example:
        To create a square with side length 5:
        square = Square(5)

    Attributes:
        side_length (int): The length of the square's sides.

    """

    def __init__(self, side_length):
        """Initialize a square with the given side length.

        Args:
            side_length (int): The length of the square's sides.

        """
        self.side_length = side_length

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.side_length ** 2

    def calculate_perimeter(self):
        """Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.

        """
        return 4 * self.side_length

