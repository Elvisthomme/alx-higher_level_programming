#!/usr/bin/python3

"""Geometry module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Create a new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of a rectangle"""
        return self.__size ** 2
