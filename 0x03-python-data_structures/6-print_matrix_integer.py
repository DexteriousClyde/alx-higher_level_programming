#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in matrix:
        for r in c:
            print("{:d}".format(r), end=" " if r != c[-1] else "")
        print()
