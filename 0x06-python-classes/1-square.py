#!/usr/bin/python3
"""Square module"""

class Square:
    """Square with size property"""

    __init__(self, size):
        self.size = size

    @property
    """The size of the square"""
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
