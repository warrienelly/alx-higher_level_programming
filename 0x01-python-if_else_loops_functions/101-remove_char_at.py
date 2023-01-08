#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for chr in range(len(str)):
        if chr!=n:
            new_str = new_str + str[chr]
    return(new_str)