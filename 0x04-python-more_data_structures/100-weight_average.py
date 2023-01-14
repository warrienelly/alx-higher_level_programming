#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_list = 0
    avg_list = 0
    if len(my_list) != 0:
        for value in my_list:
            sum_list = sum_list + value[0]*value[1]
            avg_list = avg_list + value[1]
        return sum_list/avg_list
    else:
        return 0