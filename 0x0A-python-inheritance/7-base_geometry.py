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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
