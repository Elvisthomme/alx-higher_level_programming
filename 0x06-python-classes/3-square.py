#!/usr/bin/python3
"""Square module"""


class Square:
    """Square with size property"""

    def __init__(self, size=0):
        """Create a new square with size"""
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
         """Return the current square area"""
         return self.__size ** 2
