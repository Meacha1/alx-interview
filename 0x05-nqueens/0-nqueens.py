#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(col):
        if col == N:
            solutions.append([[i, row] for i, row in enumerate(board) if 1 in row])
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions

def print_solutions(N):
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    print_solutions(N)
