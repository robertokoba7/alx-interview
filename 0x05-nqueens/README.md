N Queens
---
The N–queens puzzle is the problem of placing N chess queens on an N × N chessboard so that no two queens threaten each other. Thus, the solution requires that no two queens share the same row, column, or diagonal.

For example, for a standard 8 × 8 chessboard, below is one such configuration:

  Q  –  –  –  –  –  –  –
  –  –  –  –  Q  –  –  –
  –  –  –  –  –  –  –  Q
  –  –  –  –  –  Q  –  –
  –  –  Q  –  –  –  –  –
  –  –  –  –  –  –  Q  –
  –  Q  –  –  –  –  –  –
  –  –  –  Q  –  –  –  –
Note that the solution exists for all natural numbers n, except for n = 2 and n = 3.

Practice This Problem

 
We can solve this problem with the help of [backtracking](https://en.wikipedia.org/wiki/Backtracking). The idea is to start from the first row and place Queen in each square of the first row and recursively explore the remaining rows to check if they lead to the solution or not. If the current configuration doesn’t result in a solution, backtrack. Before exploring any square, ignore the square if two queens threaten each other.
