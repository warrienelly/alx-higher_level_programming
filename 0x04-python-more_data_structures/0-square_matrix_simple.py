#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len(matrix[0])

    row_list = []
    for row_val in range(row):
        col_list = []
        for col_val in range(col):
            col_list.append((matrix[row_val][col_val]**2))
        row_list.append(col_list)
    return row_list
