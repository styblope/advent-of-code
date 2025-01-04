#!/usr/bin/env python3
# https://adventofcode.com/2024/day/22

import sys
from collections import defaultdict

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
data = list(map(int, open(filename, "r")))


def generate(secret):
    s1 = ((secret * 64) ^ secret) % 16777216
    s2 = ((s1 // 32) ^ s1) % 16777216
    return ((s2 * 2048) ^ s2) % 16777216


# part 1
for secret in data:
    for i in range(2000):
        secret = generate(secret)
    sum1 += secret

# part 2
# TODO bit-encode seq string for dict hashing
sums = defaultdict(int)
for secret in data:
    sequences = set()
    prev = 0
    seq = []
    current = secret
    for i in range(2000 + 1):
        price = current % 10
        change = price - prev
        seq.append(change)
        if i >= 3:
            seq_string = str(seq)
            if seq_string not in sequences:
                sequences.add(seq_string)
                sums[seq_string] += price
            seq.pop(0)
        prev = price
        current = generate(current)

sum2 = max(sums.values())

print(sum1)
print(sum2)
