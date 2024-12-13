#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
left, right = zip(*(map(int, line.split()) for line in f))

print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))

hash = {}
for r in right:
    hash[r] = hash.get(r, 0) + 1

print(sum([i * hash.get(i, 0) for i in left]))
