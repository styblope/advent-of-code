#!/usr/bin/env python3
# https://adventofcode.com/2024/day/21

import sys
from collections import defaultdict
from functools import cache

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
data = [(line.strip(), int(line[0:3])) for line in f.readlines()]

NP = {
    " ": 0 + 0j,
    "0": 1 + 0j,
    "A": 2 + 0j,
    "1": 0 + 1j,
    "2": 1 + 1j,
    "3": 2 + 1j,
    "4": 0 + 2j,
    "5": 1 + 2j,
    "6": 2 + 2j,
    "7": 0 + 3j,
    "8": 1 + 3j,
    "9": 2 + 3j,
}
DP = {"<": 0 + 0j, "v": 1 + 0j, ">": 2 + 0j, " ": 0 + 1j, "^": 1 + 1j, "A": 2 + 1j}


def pathgen(a, b, keymap):
    ap, bp = keymap[a], keymap[b]
    res_path = []

    def recurse(ap, bp, dx=0, dy=0, path=None):
        if path is None:
            path = []
            dx = 1 if (bp - ap).real > 0 else -1
            dy = 1 if (bp - ap).imag > 0 else -1
        if bp == ap:
            res_path.append(path)
            return len(path)
        else:
            n = ap + dx
            if n.real * dx <= bp.real:
                pc = path.copy()
                pc.append((n, {-1: "<", 1: ">"}[dx]))
                recurse(n, bp, dx, dy, pc)

            n = ap + 1j * dy
            if n.imag * dy <= bp.imag:
                pc = path.copy()
                pc.append((n, {-1: "v", 1: "^"}[dy]))
                recurse(n, bp, dx, dy, pc)

    recurse(ap, bp)
    for r in res_path:
        p, s = zip(*r) if r else ([], [""])
        if keymap[" "] not in p:
            yield "".join(s) + "A"


@cache
def stage(key_sequence, depth, keymap="DP"):
    keymap = NP if keymap == "NP" else DP
    prev = "A"
    lens = defaultdict(int)
    ksum = 0
    for key in key_sequence:
        lens.clear()
        for i, path in enumerate(pathgen(prev, key, keymap)):
            psum = 0
            if depth > 0:
                psum = stage(path, depth - 1)
            else:
                psum += len(path)
            lens[i] = psum
        prev = key
        ksum += min(lens.values())
    return ksum


for r in 2, 25:
    print(sum(stage(keys, r, "NP") * numeric for keys, numeric in data))
