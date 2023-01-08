#!/usr/bin/python3
def islower(c):
    # check if c is in the range of small letters
    if ord(c) in range(97, 123):
        return(True)
    else:
        return(False)