#!/usr/bin/python3
"""
0. N queens
"""
import sys


def backtracking(board, row=0, column=0):
    """
    method that uses the backtracking algorithm to obtain
    all possible solutions
    """
    if row == len(board):
        print_result(board)
        return

    if row == 0:
        for column in range(len(board)):
            board[row][column] = 1
            backtracking(board, row + 1, 0)
            board[row][column] = 0

    else:
        for column in range(len(board)):
            if comprobation(board, row, column):
                board[row][column] = 1
                backtracking(board, row + 1, 0)
                board[row][column] = 0


def comprobation(board, row, column):
    """
    method that checks if the queen is being attacked,
    vertically or diagonally on both sides
    """
    for row_2 in range(len(board)):
        if board[row_2][column] == 1:
            return False

    row_2 = row
    column_2 = column
    if row != len(board) - 1 or column != 0:
        while row_2 > 0 and column_2 > 0:
            row_2 -= 1
            column_2 -= 1

        while row_2 < len(board) and column_2 < len(board):
            if board[row_2][column_2] == 1:
                return False
            row_2 += 1
            column_2 += 1

    row_2 = row
    column_2 = column
    if row != len(board) - 1 or column != len(board) - 1:
        while row_2 > 0 and column_2 < len(board) - 1:
            row_2 -= 1
            column_2 += 1

        while row_2 < len(board) and column_2 >= 0:
            if board[row_2][column_2] == 1:
                return False
            row_2 += 1
            column_2 -= 1

    return True


def print_result(board):
    """
    Method that prints the location of the queen
    through its row and column
    """
    result = []
    for row in board:
        result.append([board.index(row), row.index(1)])

    print(result)


def validate_integer(number):
    """

    """
    try:
        number = int(number)
        return number
    except ValueError:
        return 1
    except TypeError:
        return 1


argc = len(sys.argv)
argv = sys.argv

if argc != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = validate_integer(argv[1])

if n == 1:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


board = []
row = []

for i in range(n):
    for j in range(n):
        row.append(0)
    board.append(row)
    row = []

backtracking(board)
