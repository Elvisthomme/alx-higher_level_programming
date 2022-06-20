#!/usr/bin/python3
for a in "abcdefghijklmnopqrstuvwxyz":
    if a in ['q', 'e']:
        continue
    print("{}".format(a), end="")
