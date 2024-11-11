import random
from sudoku_solver import SudokuSolver

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def generate_random_problem():
    # Generate a random Sudoku problem
    problem = [[0] * 9 for _ in range(9)]
    for i in range(17):  # Randomly fill 17 cells
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid_move(problem, row, col, num):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
        problem[row][col] = num
    return problem

def is_valid_move(grid, row, col, num):
    # Check if placing 'num' at (row, col) is valid
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def main():
    print("Welcome to Sudoku Solver!")

    choice = input("Do you want to (1) input your own Sudoku problem or (2) generate a random problem? Enter 1 or 2: ")

    if choice == '1':
        print("Enter your Sudoku problem row by row (use 0 for empty cells):")
        problem = []
        for _ in range(9):
            row = list(map(int, input().split()))
            problem.append(row)
    elif choice == '2':
        problem = generate_random_problem()
    else:
        print("Invalid choice. Exiting...")
        return

    print("\nSudoku Problem:")
    print_grid(problem)

    solver = SudokuSolver(problem)
    solution = solver.solve()

    if solution:
        print("\nSolution:")
        print_grid(solution)

if __name__ == "__main__":
    main()