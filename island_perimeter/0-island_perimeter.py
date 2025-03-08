#!/usr/bin/python3
"""
Calculate the perimeter of the island described in the grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A grid where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check each of the four possible sides
                if r == 0 or grid[r - 1][c] == 0:  # Top
                    perimeter += 1
                # Bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
