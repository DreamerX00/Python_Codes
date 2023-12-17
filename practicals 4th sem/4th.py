def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]
  
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
  
    # Check the lower diagonal on the left side
    i = row
    j = col
    while j >= 0 and i < 4:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1
  
    return True


def solve_queens(board, col):
    # Base case: If all queens are placed, return True
    if col >= 4:
        return True
  
    # Recursive case
    for i in range(4):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1
  
            # Recur to place the rest of the queens
            if solve_queens(board, col + 1):
                return True
  
            # If placing queen at board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0
  
    # If no queen can be placed in this column, return False
    return False


def print_solution(board):
    # Print the board
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()


def solve_4_queen():
    # Create a 4x4 chessboard with all cells initialized to 0
    board = [[0] * 4 for _ in range(4)]
  
    # Solve the 4-Queen Problem
    if not solve_queens(board, 0):
        print("No solution exists.")
    else:
        print_solution(board)


# Solve the 4-Queen Problem
solve_4_queen()
