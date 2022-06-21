#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except BaseException:
        return i
    else:
        return x
    finally:
        print('')
