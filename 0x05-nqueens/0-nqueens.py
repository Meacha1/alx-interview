#!/usr/bin/python3
import sys 

def is_valid(board, row, col):
  # Check if there is a queen in the same column
  for i in range(len(board)):
    if board[i][col] == 'Q':
      return False
  
  # Check diagonals
  for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
    if board[i][j] == 'Q':
      return False

  for i, j in zip(range(row,len(board),1), range(col,-1,-1)):
    if board[i][j] == 'Q':
      return False

  return True

def solve_nqueens(size):
  
  board = [['.' for i in range(size)] for i in range(size)]

  solutions = []

  def backtrack(row):
    if row == size:
      solution = []
      for i in range(size):
        for j in range(size):
          if board[i][j] == 'Q':
            solution.append([i,j]) 
      solutions.append(solution)
      return

    for col in range(size):
      if is_valid(board, row, col):
        board[row][col] = 'Q'
        backtrack(row+1)
        board[row][col] = '.'

  backtrack(0)

  for solution in solutions:
    print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(size)