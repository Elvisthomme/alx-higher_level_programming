#!/bin/usr/python3

"""0x0A-python-inheritance module"""

class MyList(list):
    """A subclass of list"""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)"""
        d = self.copy()
        d.sort()
        return d
