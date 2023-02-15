#!/usr/bin/python3
'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    '''
    rotate matrix using a copy as a reference
    '''
    n = len(matrix)
    copy = [[x for x in row] for row in matrix]
    for i in range(0, n):
        for j in range(0, n):
            matrix[j][n-1-i] = copy[i][j]
