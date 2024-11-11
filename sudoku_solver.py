class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        if not self.is_valid():
            print("Invalid Sudoku grid!")
            return None
        if self.solve_sudoku():
            return self.grid
        else:
            print("No solution exists!")
            return None

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku():
                    return True
                self.grid[row][col] = 0

        return False

    def is_safe(self, row, col, num):
        return (
            self.is_valid_row(row, num)
            and self.is_valid_col(col, num)
            and self.is_valid_box(row - row % 3, col - col % 3, num)
        )

    def is_valid_row(self, row, num):
        return num not in self.grid[row]

    def is_valid_col(self, col, num):
        for row in range(9):
            if self.grid[row][col] == num:
                return False
        return True

    def is_valid_box(self, start_row, start_col, num):
        for row in range(3):
            for col in range(3):
                if self.grid[row + start_row][col + start_col] == num:
                    return False
        return True

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self):
        # Check rows and columns
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if self.grid[i][j] != 0 and self.grid[i][j] in row_set:
                    return False
                row_set.add(self.grid[i][j])

                if self.grid[j][i] != 0 and self.grid[j][i] in col_set:
                    return False
                col_set.add(self.grid[j][i])

        # Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_set = set()
                for k in range(3):
                    for l in range(3):
                        if self.grid[i + k][j + l] != 0 and self.grid[i + k][j + l] in box_set:
                            return False
                        box_set.add(self.grid[i + k][j + l])

        return True