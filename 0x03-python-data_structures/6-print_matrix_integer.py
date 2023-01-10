#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])

    for row_val in range(row):
        for col_val in range(col):
            if (col_val == col - 1):
                terminate = ""
            else:
                terminate = " "
            print('{:d}'.format(matrix[row_val][col_val]), end=terminate)
        print()
