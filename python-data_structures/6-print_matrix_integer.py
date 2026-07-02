#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ""
        for i in range(len(row)):
            if i == len(row) - 1:
                line += "{:d}".format(row[i])
            else:
                line += "{:d} ".format(row[i])
        print(line)
