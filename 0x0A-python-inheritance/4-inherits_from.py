#!/usr/bin/python3

"""0x0A-python-inheritance module"""


def inherits_from(obj, a_class):
    """Verify that obj inherits from a_class"""
    return(
              ((obj).__class__.__name__ != a_class.__name__)
              and issubclass((obj).__class, a_class)
          )
