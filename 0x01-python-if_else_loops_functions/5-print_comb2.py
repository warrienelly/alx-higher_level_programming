#!/usr/bin/python3
for number in range(0,100):
    if number < 10:
        print('{}{:d}'.format(0, number), end=', ')
    else:
        print('{:d}'.format(number), end=', ')