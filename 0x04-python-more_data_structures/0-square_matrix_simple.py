#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        squares = [num**2 for num in arr]
        new_matrix.append(squares)
    return new_matrix
