#!/usr/bin/python3
"""
BACKTRACKING ALGORITHM IN SOLVING N QUEENS.
"""
import sys


class NQueens:
    """
    implementation of n-queens using backtrackin alorithm
    """

    def __init__(self, N):
        # Initialize the board size and an empty board list
        self.N = N
        self.board = [-1] * N

    def is_safe(self, i, j):
        # Check if it's safe to place a queen at row i and column j
        for row in range(i):
            if self.board[row] == j or self.board[row] - j == row - i or self.board[row] - j == i - row:
                return False
        return True

    def place_queen(self, i):
        # Recursive function to place queens one by one
        if i == self.N:
            # All queens have been placed successfully
            return True
        for j in range(self.N):
            if self.is_safe(i, j):
                # Place the queen at row i and column j
                self.board[i] = j
                # Try placing the next queen
                if self.place_queen(i+1):
                    return True
                # Backtrack if placing the next queen didn't work
                self.board[i] = -1
        # No safe placement found for this row
        return False

    def solve(self):
        # Call the recursive function to find the solution
        if self.place_queen(0):
            # Print the board with "Q" representing queens and "." representing empty spaces
            for row in range(self.N):
                for col in range(self.N):
                    if self.board[row] == col:
                        print("Q", end=" ")
                    else:
                        print(".", end=" ")
                print()
        else:
            print("No solution found")
