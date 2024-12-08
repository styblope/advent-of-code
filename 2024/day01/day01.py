#!/usr/bin/env python3

with open("input", "r") as f:
    left, right = zip(*(map(int, line.split()) for line in f))

sum1 = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
print(sum1)

hash = {}
for r in right:
    hash[r] = hash.get(r, 0) + 1

sum2 = sum([i * hash.get(i, 0) for i in left])
print(sum2)
