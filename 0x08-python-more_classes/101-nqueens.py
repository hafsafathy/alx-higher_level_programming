#!/usr/bin/python3

"""Solves N-queens
"""
import sys


def start(n):
    """Initialize"""
    b = []
    [b.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in b]
    return (b)


def nexts(b):
    """Return"""
    if isinstance(b, list):
        return list(map(nexts, b))
    return (board)


def solu(b):
    """Return"""
    res = []
    for r in range(len(b)):
        for c in range(len(b)):
            if b[r][c] == "Q":
                res.append([r, c])
                break
    return (res)


def vv(b, row, col):
    """
    """

    for c in range(col + 1, len(b)):
        b[row][c] = "x"
    
    for c in range(col - 1, -1, -1):
        b[row][c] = "x"
    
    for r in range(row + 1, len(b)):
        b[r][col] = "x"

    for r in range(row - 1, -1, -1):
        b[r][col] = "x"
    
    c = col + 1
    for r in range(row + 1, len(b)):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        b[r][c]
        c -= 1
    
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    
    c = col - 1
    for r in range(row + 1, len(b)):
        if c < 0:
            break
        b[r][c] = "x"
        c -= 1


def lasts(b, row, queens, solutions):
    """solve N-queens puzzle
    """
    if queens == len(b):
        solutions.append(solu(b))
        return (solutions)

    for c in range(len(b)):
        if b[row][c] == " ":
            tmp_board = nexts(b)
            tmp_board[row][c] = "Q"
            vv(tmp_board, row, c)
            solutions = lasts(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    b = start(int(sys.argv[1]))
    solutions = lasts(b, 0, 0, [])
    for s in solutions:
        print(s)
