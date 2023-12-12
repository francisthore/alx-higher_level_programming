#!/usr/bin/python3
"""This is a module that divides a matrix
    It checks if the list is ints and floats only
    Tests will be written to check
    And so help us God
"""


def matrix_divided(matrix, div):
    """This function divides a matrix
        Returns a new matrix of answers
    """
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
                                 of integers/floats")
    res_final = []
    for sub_list in matrix:
        res_tmp = []
        for idx in range(len(sub_list)):
            res_tmp.append(round((sub_list[idx] / div), 2))
        res_final.append(res_tmp)
    return res_final
