#!/usr/bin/python3
class Square:
    """Empty square class"""

    __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
