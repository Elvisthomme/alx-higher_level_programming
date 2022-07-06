#!/usr/bin/python3

"""0x0A-python-inheritance module"""


def is_same_class(obj, a_class):
    """Verify that obj is an instance of a_class"""
    return (obj).__class__.__name__ == a_class.__name__
