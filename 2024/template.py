#!/usr/bin/env python3
import sys

sum1 = sum2 = 0

with open(sys.argv[1], "r") as f:
    grid = [line.strip() for line in f.readlines()]


print(sum1)
print(sum2)

