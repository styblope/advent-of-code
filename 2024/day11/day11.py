#!/usr/bin/env python3
# https://adventofcode.com/2024/day/11
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
digits = f.read().strip().split()

memoize = dict()


def rule(d):
    if d == "0":
        return "1", None
    elif len(d) % 2 == 0:
        return str(int(d[: len(d) // 2])), str(int(d[len(d) // 2 :]))
    return str(int(d) * 2024), None


def blink(stone, count):
    global memoize
    res = memoize.get((stone, count), 0)
    if res > 0:
        return res

    a = stone
    for c in range(count):
        a, b = rule(a)
        if b is not None:
            res += 1 + blink(b, count - c - 1)

    if res > 0:
        memoize[(stone, count)] = res
    return res


def stones(digits, blinks):
    ndl = list(zip(digits, [blinks] * len(digits)))
    return len(digits) + sum(blink(a, count) for a, count in ndl[::-1])


print(stones(digits, 25))
print(stones(digits, 75))
