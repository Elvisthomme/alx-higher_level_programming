#!/usr/bin/python3

"""My integer module"""


class MyInt(int):
    """Rebel interger class"""
    def __eq__(self, other):
        """inverse equal"""
        return self != other

    def __ne__(self, other):
        """inverse not equal"""
        return self == other
