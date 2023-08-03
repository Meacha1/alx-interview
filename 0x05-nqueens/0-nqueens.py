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

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
  
  n = 0
  try:
    n = int(sys.argv[1])  
  except:
    print("N must be a number")
    sys.exit(1)  
  
  if n < 4:
    print("N must be at least 4")
    sys.exit(1)

  solve_nqueens(n)