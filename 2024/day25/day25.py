#!/usr/bin/env python3
# https://adventofcode.com/2025/day/25

from os import walk
import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
grids = f.read().strip().split("\n\n")
W = 5
H = 7

keys = []
locks = []
for grid in grids:
    counts = list(map(lambda x: x.count("#"), zip(*grid.split("\n"))))
    heights = [c - 1 for c in counts]

    if grid[0:W] == "#" * W:
        locks.append(heights)
    else:
        keys.append(heights)

for key in keys:
    for lock in locks:
        sum1 += all(key[i] + lock[i] <= 5 for i in range(W))

print(sum1)
print(sum2)
