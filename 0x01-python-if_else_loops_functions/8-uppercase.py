#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for chr in str:
        if ord(chr) in range(97, 123):
            new_str = new_str + '{:c}'.format((ord(chr) - 32))
        else:
            new_str = new_str + chr
    print(new_str)
