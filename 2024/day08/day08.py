#!/usr/bin/env python3
# https://adventofcode.com/2024/day/8
import itertools
from operator import sub
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
grid = [line.strip() for line in f.readlines()]

sum1 = sum2 = 0
X, Y = len(grid[0]), len(grid)

hm = {}
for y, line in enumerate(grid):
    for x, k in enumerate(line):
        if k.isalnum():
            hm.setdefault(k, set()).add((x, y))


def diff(a, b):
    return tuple(map(sub, a, b))


res = set()
for k, pos in hm.items():
    res.update(pos)
    for a, b in itertools.permutations(pos, 2):
        dist = diff(b, a)
        anode = diff(a, dist)
        while 0 <= anode[0] < X and 0 <= anode[1] < Y:
            if anode not in pos:
                pos.add(anode)
                res.add(anode)
            anode = diff(anode, dist)

sum2 = len(res)
print(sum2)
