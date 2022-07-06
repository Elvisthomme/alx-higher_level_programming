#!/usr/bin/python3

"""0x0A-python-inheritance module"""


def is_kind_of_class(obj, a_class):
    """Verify that obj is an instance of a_class
       or a subclass of a_class"""
    return issubclass((obj).__class__, a_class)
