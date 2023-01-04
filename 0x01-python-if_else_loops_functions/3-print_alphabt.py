#!/usr/bin/python3
for as_code in range(97, 123):
    if as_code not in [101, 113]:
        print("{:c}".format(as_code), end='')
