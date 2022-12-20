#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    triangle = []  # create an empty triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(i - 1):
                row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            row.append(1)
            triangle.append(row)

    return triangle
