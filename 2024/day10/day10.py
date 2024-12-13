#!/usr/bin/env python3
# https://adventofcode.com/2024/day/10
import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
grid = [int(x) if x != "\n" else 99 for x in f.read()]

W = grid.index(99) + 1
LEN = len(grid)
zeros = [p for p, d in enumerate(grid) if d == 0]


def recurse(p):
    global score, sum2
    if grid[p] == 9:
        score.add(p)
        sum2 += 1
        return

    dirs = {
        p - W: p - W > 0 and grid[p - W] == grid[p] + 1,
        p + W: p + W < LEN - 1 and grid[p + W] == grid[p] + 1,
        p + 1: grid[p + 1] < 99 and grid[p + 1] == grid[p] + 1,
        p - 1: grid[p - 1] < 99 and grid[p - 1] == grid[p] + 1,
    }

    [recurse(k) for k, v in dirs.items() if v]


for p in zeros:
    score = set()
    recurse(p)
    sum1 += len(score)

print(sum1)
print(sum2)
