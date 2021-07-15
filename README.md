# python-sudoku-solver
Practicing backtracking with a sudoku solution solver

Strategy
1. Pick an empty square
2. Try all numbers
3. Find one that works
4. Repeat
5. Backtrack to the last step and try an alternate number, repeating the process


# Tests
1. Install pytest
2. To run test files, enter $python -m pytest in the command line
3. To see a summary of the result of all test, including passes, use $python -m pytest -rA