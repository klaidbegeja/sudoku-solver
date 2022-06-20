# Sudoku rules are simple and straightforward. 
# It is precisely their simplicity that makes finding the solution and solving these puzzles a true challenge.
# Rule 1 - Each row must contain the numbers from 1 to 9, without repetitions
# Rule 2 - Each column must contain the numbers from 1 to 9, without repetitions
# Rule 3 - The digits can only occur once per block 


def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0:
            print("#+-------+-------+-------+")
        print("#|", end="")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" |", end="")
            if j == 8:
                print(" " + str(grid[i][j]) + " |") 
            else:
                print(" " + str(grid[i][j]), end="")
    print("#+-------+-------+-------+")

def find_next_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None, None

def possible(grid, n, row, col):
    row_vals = grid[row]
    if n in row_vals:
        return False
    
    col_vals = [grid[i][col] for i in range(9)]
    if n in col_vals:
        return False

    row_start = (row//3) * 3
    col_start = (col//3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == n :
                return False
    return True

def solver(grid):
    row, col = find_next_empty(grid)
    if row is None:
        return True
    for n in range(1,10):
        if possible(grid, n, row, col):
            grid[row][col] = n
            if solver(grid):
                return True                            
        grid[row][col] = 0
    return False


grid = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

grid2 = [
  [0, 9, 0, 4, 3, 0, 0, 0, 0],
  [0, 0, 8, 0, 0, 5, 0, 0, 6],
  [0, 0, 5, 6, 0, 9, 1, 0, 0],
  [0, 0, 9, 0, 0, 0, 0, 2, 1],
  [0, 8, 3, 0, 0, 0, 6, 7, 0],
  [5, 4, 0, 0, 0, 0, 9, 0, 0],
  [0, 0, 4, 5, 0, 3, 2, 0, 0],
  [3, 0, 0, 7, 0, 0, 8, 0, 0],
  [0, 0, 0, 0, 1, 6, 0, 5, 0]
]
print('##########################')
print('Initial Gid')
print('##########################')
print_grid(grid2)
solver(grid2)
print('##########################')
print('Solved sudoku')
print('##########################')
print_grid(grid2)