# Sudoku Solver

## Description
This Sudoku Solver program is designed to solve Sudoku puzzles using a Constraint Satisfaction Problem (CSP) approach with backtracking and constraint propagation. It allows users to input their own Sudoku puzzle or generate a random one for the program to solve.

## Valid Input
The program assumes that the user provides a valid Sudoku puzzle as input. A valid Sudoku puzzle should adhere to the standard Sudoku rules:
The grid should be a 9x9 matrix.
Each cell should contain a number from 1 to 9 or 0 to represent an empty cell.
Each row, column, and 3x3 subgrid should contain unique numbers from 1 to 9.

## User Input
If the user chooses to input their own Sudoku problem:
The user should input the Sudoku grid row by row.
Use '0' to represent empty cells.
Each row should contain 9 numbers separated by spaces.

## Random Problem Generation
If the user chooses to generate a random Sudoku problem:
The program generates a Sudoku problem by randomly filling 17 cells in a 9x9 grid.
It ensures that the generated problem adheres to Sudoku rules, with no conflicting numbers in rows, columns, or subgrids.

## Solution
The program uses a backtracking algorithm with constraint propagation to find the solution.
If a solution exists, it will be displayed.
If no solution exists for the given problem, the program will notify the user.

## Output
The program displays the Sudoku problem provided by the user or generated randomly.
It then displays the solution, if found.

## Running the Program
Ensure you have Python installed on your system.
Download the sudoku_solver.py and main.py files.
Run main.py using Python: python main.py.
Follow the prompts to input your Sudoku problem or choose to generate a random one.
View the problem and its solution displayed by the program.
