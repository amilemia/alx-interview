#!/usr/bin/python3
"""Island Perimeter Problem"""


def search_land(grid):
    """Searches for land"""
    visited = set()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                return calc_perimeter(grid, x, y, visited)
    return 0


def calc_perimeter(grid, x, y, visited):
    """Calculates perimeter
        if cell == 0: +1 perimeter
        if cell is in visited: skip
        if cell == 1: go to top, left, bottom, right => recursion
    """
    if x >= len(grid) or y >= len(grid[x]) or x < 0 or y < 0 \
       or grid[x][y] == 0:
        return 1

    if (x, y) in visited:
        return 0

    visited.add((x, y))

    perimeter = calc_perimeter(grid, x, y - 1, visited)
    perimeter += calc_perimeter(grid, x, y + 1, visited)
    perimeter += calc_perimeter(grid, x - 1, y, visited)
    perimeter += calc_perimeter(grid, x + 1, y, visited)

    return perimeter


def island_perimeter(grid):
    """Calculates the perimeter of an island"""
    return search_land(grid)
