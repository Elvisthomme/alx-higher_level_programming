#!/usr/bin/python3

"""Geometry module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """area of BaseGeomety"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """interger validator"""
        if (value).__class__.__name__ != int.__name__:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
