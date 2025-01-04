#!/usr/bin/env python3
# https://adventofcode.com/2024/day/19

import sys
import re
from functools import cache

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
raw_patterns, _, *designs = [line.strip() for line in open(filename, "r")]
patterns = raw_patterns.split(", ")

@cache
def all_matches(subdesign):
    global patterns
    if not subdesign:
        return 1

    count = 0
    for pattern in patterns:
        if subdesign.startswith(pattern):
            next = subdesign[len(pattern) :]
            # mem = memoize.get(next)
            # count += mem if mem is not None else all_matches(next, patterns)
            count += all_matches(next)
    # memoize[subdesign] = count
    return count


# memoize = dict()
sum1 = sum(1 for design in designs if re.fullmatch(r"(%s)+" % r"|".join(patterns), design))
sum2 = sum(all_matches(design) for design in designs)
print(sum1)
print(sum2)
