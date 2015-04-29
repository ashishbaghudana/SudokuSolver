# SudokuSolver
A simple Sudoku Solver using Backtracking, written in Python.

Give an input as following:
<number of test cases>
<9 lines of the sudoku, where an empty cell is given by 0>

For example:
```
1
4 0 0 0 0 6 0 0 0
0 6 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 3 0 6 0 0 2 0
1 0 0 0 0 0 9 0 0
8 0 0 0 0 5 0 0 0
0 0 0 0 0 0 0 0 5
```
represents the Sudoku given by:<br />
```
  4 . . | . . 6 | . . .
  . . 6 | . . . | . . 9
  . . . | . . . | . . .
  ------+-------+------
  . . 2 | . . . | . . .
  . . . | . . . | . . .
  . . 3 | . 6 . | . 2 .
  ------+-------+------
  1 . . | . . . | 9 . .
  8 . . | . . 5 | . . .
  . . . | . . . | . . 5
```
gives an output of:<br />
```
  4 1 5 2 9 6 3 7 8
  2 6 7 1 3 8 4 5 9
  3 9 8 4 5 7 1 6 2
  5 4 2 3 7 1 8 9 6
  6 7 1 8 2 9 5 3 4
  9 8 3 5 6 4 7 2 1
  1 5 6 7 4 2 9 8 3
  8 3 9 6 1 5 2 4 7
  7 2 4 9 8 3 6 1 5
```
representing:<br />
```
  4 1 5 | 2 9 6 | 3 7 8
  2 6 7 | 1 3 8 | 4 5 9
  3 9 8 | 4 5 7 | 1 6 2
  ------+-------+------
  5 4 2 | 3 7 1 | 8 9 6
  6 7 1 | 8 2 9 | 5 3 4
  9 8 3 | 5 6 4 | 7 2 1
  ------+-------+------
  1 5 6 | 7 4 2 | 9 8 3
  8 3 9 | 6 1 5 | 2 4 7
  7 2 4 | 9 8 3 | 6 1 5
```
The solver produces an output only if the Sudoku has a solution, otherwise it returns False.
