#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        f1_char = None
    else:
        f1_char = sentence[0]
    return (length, f1_char)
