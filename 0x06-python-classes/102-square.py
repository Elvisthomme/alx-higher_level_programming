#!/usr/bin/python3
"""Square module"""


class Square:
    """Square with size property"""

    def __init__(self, size=0):
        """Create a new square with size"""
        self.size = size

    @property
    def size(self):
        """The size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
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

    def __eq__(self, other):
        """Return whether self is equal to other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return whether self is not equal to other"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return whether self is grether than other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return whether self is grether or equal to other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Return whether self is less than other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Return whether self is less or equal to other"""
        return self.area() <= other.area()
