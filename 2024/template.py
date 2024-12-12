#!/usr/bin/env python3
# https://adventofcode.com/YYYY/day/DD

import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else 'input'
f = open(filename, "r")
grid = [line.strip() for line in f.readlines()]


print(sum1)
print(sum2)

