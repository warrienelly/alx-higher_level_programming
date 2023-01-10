#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return None
    for interger in my_list[::-1]:
        print("{:d}".format(interger))
