#!/usr/bin/env python3
# https://adventofcode.com/2024/day/15

import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
grid, p2 = open(filename, "r").read().split("\n\n")
resized_grid = "".join(
    {"#": "##", "O": "[]", ".": "..", "@": "@.", "\n": "\n"}[m] for m in grid
)
movements = "".join(p2.split())


def shift(p, d, map):
    i = d
    while True:
        gap = p + d + i
        if map[gap] == ".":
            map[gap] = "O"
            return True
        elif map[gap] == "#":
            break
        i += d


def show(map):
    for i, m in enumerate(map):
        print(m, end="")
        if i % W == W:
            print()
    print()


grid = list(grid)
W = grid.index("\n") + 1
bot = grid.index("@")
for move in movements:
    d = {">": 1, "<": -1, "^": -W, "v": W}[move]

    if grid[bot + d] == "#":
        continue
    if grid[bot + d] == "." or grid[bot + d] == "O" and shift(bot, d, grid):
        grid[bot] = "."
        bot += d
        grid[bot] = "@"

print(sum([100 * (p // W) + p % W for p, m in enumerate(grid) if m == "O"]))


# part 2
def shift2(bot, d, grid):
    if grid[bot + d + d] == "#":
        return False
    if d == 1 or d == -1:
        i = d
        while True:
            gap = bot + d + 2 * i
            if grid[gap] == ".":
                grid.pop(gap)
                grid.insert(bot, ".")
                return True
            elif grid[gap] == "#":
                break
            i += d

    # d == W or d == -W
    else:
        if grid[bot + d] == "]":
            bot -= 1
        cluster = {bot + d, bot + d + 1}
        cluster = expand(bot + d, d, cluster, grid)

        fill = set({t + d for t in cluster}) - cluster
        if all(grid[f] == "." for f in fill):
            for c in sorted(cluster, reverse=d > 0):
                grid[c + d], grid[c] = grid[c], grid[c + d]
            return True
        elif any(grid[f] == "#" for f in fill):
            return False


def expand(n, d, cluster, grid):
    if grid[n + d] == "[":
        cluster.add(n + d)
        cluster.add(n + d + 1)
        expand(n + d, d, cluster, grid)
        return cluster

    if grid[n + d] == "]":
        cluster.add(n + d)
        cluster.add(n + d - 1)
        expand(n + d - 1, d, cluster, grid)
    if grid[n + d + 1] == "[":
        cluster.add(n + d + 1)
        cluster.add(n + d + 2)
        expand(n + d + 1, d, cluster, grid)
    return cluster


grid = list(resized_grid)
W = grid.index("\n") + 1
bot = grid.index("@")
# show(grid)
for move in movements:
    d = {">": 1, "<": -1, "^": -W, "v": W}[move]

    if grid[bot + d] == "#":
        continue
    if grid[bot + d] == "." or grid[bot + d] in ["[", "]"] and shift2(bot, d, grid):
        grid[bot] = "."
        bot += d
        grid[bot] = "@"
    # show(grid)

print(sum([100 * (p // W) + p % W for p, m in enumerate(grid) if m == "["]))
