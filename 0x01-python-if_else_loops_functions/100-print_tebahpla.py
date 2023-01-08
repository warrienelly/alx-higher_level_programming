#!/usr/bin/python3
for chr in range(122, 96, -1):
    if (chr % 2 == 0):
        print('{:c}'.format(chr), end="")
    else:
        print('{:c}'.format(chr-32), end="")
