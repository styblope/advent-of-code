#!/usr/bin/env python3
# https://adventofcode.com/2024/day/13
import sys
import re
from itertools import batched

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
digits = list(map(int, re.findall(r"\d+", open(filename, "r").read())))
machines = list(batched(batched(digits, 2), 3))


def solve(machine, add=0):
    """Solve using set of two linear equations"""
    a, b, prize = machine
    ax, ay = a
    bx, by = b
    px, py = (p + add for p in prize)

    y = (ay * px - ax * py) / (bx * ay - ax * by)
    x = (px - bx * y) / ax
    return 3 * int(x) + int(y) if x.is_integer() and y.is_integer() else 0


print(sum(solve(machine) for machine in machines))
print(sum(solve(machine, add=10000000000000) for machine in machines))
