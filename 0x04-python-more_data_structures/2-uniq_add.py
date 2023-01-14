#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for value in set(my_list):
        if len(my_list) == 0:
            return None
        else:
            sum = sum + value
    return sum
