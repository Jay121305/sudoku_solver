def print_grid(grid, N):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_safe(grid, row, col, num, N):
    # Check if 'num' is not in the given row and column
    for x in range(N):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check if 'num' is not in the subgrid
    sqrt_N = int(N ** 0.5)
    start_row = row - row % sqrt_N
    start_col = col - col % sqrt_N
    for i in range(sqrt_N):
        for j in range(sqrt_N):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(grid, N):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(grid, N):
    empty = find_empty_location(grid, N)
    if not empty:
        return True
    row, col = empty

    for num in range(1, N + 1):
        if is_safe(grid, row, col, num, N):
            grid[row][col] = num
            if solve_sudoku(grid, N):
                return True
            grid[row][col] = 0  # Backtrack

    return False

def get_user_grid(N):
    print(f"Enter the Sudoku grid row by row (use 0 for empty cells):")
    grid = []
    for i in range(N):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != N:
                    print(f"Please enter exactly {N} numbers.")
                    continue
                grid.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return grid

if __name__ == "__main__":
    N = int(input("Enter size of Sudoku (e.g., 4 for 4x4, 9 for 9x9, 16 for 16x16): "))
    if int(N ** 0.5) ** 2 != N:
        print("Size must be a perfect square (4, 9, 16, 25, ...).")
    else:
        sudoku_grid = get_user_grid(N)
        print("\nOriginal Sudoku grid:")
        print_grid(sudoku_grid, N)
        if solve_sudoku(sudoku_grid, N):
            print("\nSolved Sudoku grid:")
            print_grid(sudoku_grid, N)
        else:
            print("No solution exists.")