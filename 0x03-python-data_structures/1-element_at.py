#!/usr/bin/python3
def element_at(my_list, idx):
    ls_len = len(my_list)
    if idx < 0:
        return None
    if idx > (ls_len - 1):
        return None

    return "{:d}".format(my_list[idx])