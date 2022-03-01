#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                s += 4
                if j > 0 and grid[i][j - 1] == 1:
                    s -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    s -= 2
    return s
