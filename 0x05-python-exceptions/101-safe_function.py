#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        sys.stderr.write(f"Exception: {err}\n")
    return result
