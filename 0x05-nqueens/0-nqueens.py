#!/usr/bin/python3
"""
BACKTRACKING ALGORITHM IN SOLVING N-QUEENS.
"""
import sys

class NQueens:
    """
    Implementation of nqueen 
    """
    def __init__(self, N):
        self.N = N
        self.board = [['.' for _ in range(N)] for _ in range(N)]

    def is_safe(self, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Check if there is a queen in the upper-left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # Check if there is a queen in the upper-right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, self.N)):
            if self.board[i][j] == 'Q':
                return False

        # If all checks pass, it is safe to place a queen at this position
        return True

    def place_queen(self, row):
        # Base case: if all rows are filled, a valid solution is found
        if row == self.N:
            return True

        # Try to place a queen in each column of the current row
        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                if self.place_queen(row+1):
                    return True
                self.board[row][col] = '.'

        # If no valid solution is found, backtrack
        return False

    def solve(self):
        if self.place_queen(0):
            # Print the solution
            for row in self.board:
                print(' '.join(row))
        else:
            print('No solutions found.')

if __name__ == '__main__':
    # Parse the command-line argument N
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Create an instance of the NQueens class with the given size
    nqueens = NQueens(N)

    # Call the solve method to solve the problem and print the solution
    nqueens.solve()
