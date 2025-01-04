#!/usr/bin/env python3
# https://adventofcode.com/2024/day/23

import sys
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
network = [line.strip().split("-") for line in f.readlines()]

nodes = defaultdict(set)
for a, b in network:
    nodes[a].add(b)
    nodes[b].add(a)

# part 1
triplets = set()
for a in nodes:
    for b in nodes[a]:
        for c in nodes[b]:
            if a in nodes[c] and any(n.startswith("t") for n in (a,b,c)):
                triplets.add(str(sorted((a,b,c))))

print(len(triplets))

# part 2
groups = defaultdict(int)
for node in nodes:
    for next in nodes[node]:
        common = (nodes[node] | {node}) & (nodes[next] | {next})
        groups[",".join(sorted(common))] += 1

largest = max(groups.values())
for k, v in groups.items():
    if v == largest:
        print(k)
