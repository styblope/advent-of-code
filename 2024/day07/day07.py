#!/usr/bin/env python3
# https://adventofcode.com/2024/day/7
import re
import operator
import itertools
import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
parsed = [list(map(int, re.findall(r"\d+", line))) for line in f]


OPERATORS = [operator.add, operator.mul, lambda a, b: int(f"{a}{b}")]

for row in parsed:
    test, *vals = row

    for ops in itertools.product(OPERATORS, repeat=len(vals) - 1):
        res = vals[0]
        for i, op in enumerate(ops):
            res = op(res, vals[i + 1])
            if res > test:
                break
        else:
            if res == test:
                sum2 += test
                if OPERATORS[2] not in ops:
                    sum1 += test
                break


print(sum1)
print(sum2)
