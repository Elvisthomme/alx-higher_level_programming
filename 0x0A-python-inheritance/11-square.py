#!/usr/bin/python3

"""Geometry module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """area of BaseGeomety"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """interger validator"""
        if (value).__class__.name == int.__name__:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Create a new rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Create a new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of a square"""
        return self.__size ** 2

    def __str__(self):
        """String representation of a square"""
        return "[Square] {}/{}".format(self.__width, self.__height)
