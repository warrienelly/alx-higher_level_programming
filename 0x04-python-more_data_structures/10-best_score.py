#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        largest = a_dictionary[list(a_dictionary.keys())[0]]
        largest_key = ""
        for key, value in a_dictionary.items():
            if value > largest:
                largest = value
                largest_key = key

        return largest_key
    else:
        return None

