#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    lst_key = a_dictionary.keys()
    if key in lst_key:
        del a_dictionary[key]
    return a_dictionary