#!/usr/bin/python3
import sys

def print_chessboard(queens):
  """Print the chessboard with queens in their positions"""
  for i in range(len(queens)):
    for j in range(len(queens)):
      if queens[i] == j:
        print("Q", end="")
      else:
        print("-", end="")
    print()

def is_valid(queens, row, col):
  """Check if a queen can be placed on the chessboard"""
  for i in range(row):
    if queens[i] == col or abs(queens[i] - col) == row - i:
      return False
  return True
      
def solve_nqueens(n):
  queens = [-1 for i in range(n)]
  
  def backtrack(row):
    if row == n:
      print_chessboard(queens)
      return
    
    for col in range(n):
      if is_valid(queens, row, col):
        queens[row] = col
        backtrack(row+1)

  backtrack(0)
  