#!/usr/bin/env python3
# https://adventofcode.com/2024/day/20

import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
grid = open(filename, "r").read()

W = grid.index("\n") + 1
S = grid.index("S")
E = grid.index("E")
DIRS = {1, -1, W, -W}


def dist(a, b):
    xa, ya = divmod(a, W)
    xb, yb = divmod(b, W)
    return abs(xa - xb) + abs(ya - yb)


track = [S]
p = prev = S
while p != E:
    next, *_ = [p + d for d in DIRS if grid[p + d] in [".", "E"] and p + d != prev]
    track += [next]
    prev, p = p, next

sum1 = sum(
    1
    for i, p in enumerate(track)
    for d in DIRS
    if grid[p + d] == "#"
    and p + 2 * d in track[i + 1 :]
    and track.index(p + 2 * d) - i - 2 >= 100
)


def cheats(i, r):
    return sum(
        1
        for x, p in enumerate(track[i + 100:])
        if i + 100 + x < len(track) and dist(track[i], p) <= min(x, r)
    )

#sum1 = sum(cheats(i, 2) for i,_ in enumerate(track))
sum2 = sum(cheats(i, 20) for i,_ in enumerate(track))


print(sum1)
print(sum2)
