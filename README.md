# AI-Sudoku-Solver
Sudoku solver in Python.

Pass any 8x8 board to the solveSudoku function in the main.py.

The solvers considers board as CSP (constraint satisfaction problem). 
Sudoku is solved by backtracking.
MRV (minimum remainig values) and Degree heuristic is used to choose the cell.
After every assignment of value to the variable forward checking updates domains of cells influenced by assignment.

