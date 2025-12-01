#!/usr/bin/env python3
# https://adventofcode.com/2024/day/7
import re
from operator import sub, floordiv
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
parsed = [list(map(int, re.findall(r"\d+", line))) for line in f]

trim = lambda a, b: int(str(a)[: -len(str(b))])  # noqa: E731
with_con = False

def qualified_invops(test, val):
    if test >= val:
        yield sub
        if test % val == 0:
            yield floordiv
    if with_con and test > val and str(test).endswith(str(val)):
        yield trim

def recurse(test, vals, i):
    ops = list(qualified_invops(test, vals[i]))
    for invop in ops:
        res = invop(test, vals[i])
        if i == 1 and res == vals[0]:
            return True
        if i > 1:
            if recurse(res, vals, i - 1):
                return True

sum1 = sum(test for test, *vals in parsed if recurse(test, vals, len(vals) - 1))
with_con = True
sum2 = sum(test for test, *vals in parsed if recurse(test, vals, len(vals) - 1))

print(sum1)
print(sum2)
