#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as err:
        result = None
        sys.stderr.write("Exception: {err}")
    return result
