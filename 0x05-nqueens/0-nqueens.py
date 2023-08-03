#!/usr/bin/python3
import sys

def print_board(board):
    """
    Prints the board
    """
    for row in board:
        print(" ".join(row))

def is_valid(board, row, col):
    """
    Checks if the position is valid for a queen
    """
    # Check column
    for i in range(len(board)):
        if board[i][col] == "Q":
            return False
    
    # Check diagonal
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == "Q":
            return False
    
    for i, j in zip(range(row,len(board)), range(col,-1,-1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_queens(board, row):
    """
    Solves the problem recursively
    """
    if row == len(board):
        print_board(board)
        return
    
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = "Q" 
            solve_queens(board, row+1)
            board[row][col] = "-" 
