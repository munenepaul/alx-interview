#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """This solution uses nested loops to access each
      element of the matrix and swap its values with the elements
        located at the corresponding positions in
        the rotated matrix."""

    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
