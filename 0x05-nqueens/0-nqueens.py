#!/usr/bin/python3
"""
N Queens Project
Solves the N queens puzzle: placing
N non-attacking queens on an NxN chessboard.
"""

import sys

solutions = []
n = 0
pos = None


def get_input():
    """Validates and processes the program's argument."""
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if two queens are attacking each other."""
    if pos0[0] == pos1[0] or pos0[1] == pos1[1]:
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if a group of positions already exists in solutions."""
    global solutions
    for stn in solutions:
        if sorted(stn) == sorted(group):
            return True
    return False


def build_solution(row, group):
    """Recursively builds solutions for the N queens problem."""
    global solutions, n
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
    else:
        for col in range(n):
            pos_index = row * n + col
            matches = zip([pos[pos_index]] * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            if not any(used_positions):
                group.append(pos[pos_index])
                build_solution(row + 1, group)
                group.pop()


def get_solutions():
    """Finds all solutions for the given chessboard size."""
    global pos, n
    pos = [[i // n, i % n] for i in range(n * n)]
    build_solution(0, [])


if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
