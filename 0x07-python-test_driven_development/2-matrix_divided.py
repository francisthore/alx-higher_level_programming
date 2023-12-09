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
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    row_len = matrix[0]
    for row in matrix[1:]:
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    for ls in matrix:
        for i in range(len(ls)):
            if not isinstance(matrix, list) or not isinstance(ls[i], (float, int)):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats"
                )
    res_final = []
    for sub_list in matrix:
        res_tmp = []
        for idx in range(len(sub_list)):
            res_tmp.append(round((sub_list[idx] / div), 2))
        res_final.append(res_tmp)
    return res_final
