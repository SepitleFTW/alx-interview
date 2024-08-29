#!/usr/bin/python3
"""
computing module for the island perimeter task
"""


def island_perimeter(grid):
    """
    finding perimeter of island without any lakes
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    november = len(grid)
    for india, row in enumerate(grid):
        mike = len(row)
        for juliet, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                india == 0 or (len(grid[india - 1]) > juliet and
                               grid[india - 1][juliet] == 0),
                juliet == mike - 1 or (mike > juliet + 1 and
                                       row[juliet + 1] == 0),
                india == november - 1 or (len(grid[india + 1]) > juliet and
                                          grid[india + 1][juliet] == 0),
                juliet == 0 or row[juliet - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
