#!/usr/bin/python3

"""This module computes the perimeter ojf an island given in grid form
"""


def island_perimeter(grid):
    '''This function finds the square or rectangular perimeter of an island
    '''
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Check right
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

                # Check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Check down
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
