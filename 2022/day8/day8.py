from enum import IntEnum
from math import prod


class Direction(IntEnum):
    EAST =  0
    WEST =  1
    NORTH = 2
    SOUTH = 3


def process_input():
    with open('input.txt') as f:
        return [[int(i) for i in line.strip()] for line in f.readlines()]


def is_edge(grid, n, m):
    return n == 0 or n == (len(grid) - 1) or m == 0 or m == (len(grid[n]) - 1)


def is_visible(grid, n, m):
    if is_edge(grid, n, m):
        return True

    visibility = [True] * 4

    for i in range(n - 1, -1, -1):
        if grid[i][m] >= grid[n][m]:
            visibility[Direction.EAST] = False
            break

    for i in range(n + 1, len(grid)):
        if grid[i][m] >= grid[n][m]:
            visibility[Direction.WEST] = False
            break

    for j in range(m - 1, -1, -1):
        if grid[n][j] >= grid[n][m]:
            visibility[Direction.NORTH] = False
            break

    for j in range(m + 1, len(grid[n])):
        if grid[n][j] >= grid[n][m]:
            visibility[Direction.SOUTH] = False
            break

    return any(visibility)


def calc_scenic_score(grid, n, m):
    scenic_scores = [0] * 4

    for i in range(n - 1, -1, -1):
        scenic_scores[Direction.EAST] += 1
        if grid[i][m] >= grid[n][m]:
            break

    for i in range(n + 1, len(grid)):
        scenic_scores[Direction.WEST] += 1
        if grid[i][m] >= grid[n][m]:
            break

    for j in range(m - 1, -1, -1):
        scenic_scores[Direction.NORTH] += 1
        if grid[n][j] >= grid[n][m]:
            break

    for j in range(m + 1, len(grid[n])):
        scenic_scores[Direction.SOUTH] += 1
        if grid[n][j] >= grid[n][m]:
            break

    return prod(scenic_scores)


def solution(grid):
    num_visible = 0
    scenic_scores = [[None for _ in row] for row in grid]

    for n in range(len(grid)):
        for m in range(len(grid[n])):
            if is_visible(grid, n, m):
                num_visible += 1
            scenic_scores[n][m] = calc_scenic_score(grid, n, m)

    return num_visible, max(map(max, scenic_scores))


if __name__ == '__main__':
    tree_grid = process_input()

    part1, part2 = solution(tree_grid)
    
    print(f'Part 1 solution: {part1}')
    print(f'Part 2 solution: {part2}')