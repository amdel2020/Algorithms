def matrix_search(grid, x):
    row, col = 0, len(grid[0])-1
    while row < len(grid) and col >= 0:
        if grid[row][col] == x:
            return True
        elif grid[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

grid = [[-1,2,4,4,6], [1,5,5,9,21], [3,6,6,9,22], [3,6,8,10,24], [6,8,9,12,25], [8,10,12,13,40]]
print(matrix_search(grid, 8))