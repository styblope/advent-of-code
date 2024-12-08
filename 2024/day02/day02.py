#!/usr/bin/env python3
from enum import Enum

sum1 = 0
sum2 = 0


class Trend(Enum):
    UP = 1
    DOWN = 2
    INVALID = None


def trend(diff):
    if 1 <= diff <= 3:
        return Trend.UP
    if -3 <= diff <= -1:
        return Trend.DOWN
    return Trend.INVALID


def is_safe(state):
    return all(s == Trend.UP for s in state) or all(s == Trend.DOWN for s in state)


def state(report):
    return [trend(report[i + 1] - report[i]) for i in range(len(report) - 1)]


with open("input", "r") as f:
    for line in f:
        report = list(map(int, line.split()))

        if is_safe(state(report)):
            sum1 += 1
            sum2 += 1
        else:
            # part2, less one level
            for p in range(len(report)):
                damped = [v for i, v in enumerate(report) if i != p]
                if is_safe(state(damped)):
                    sum2 += 1
                    break

print(sum1)
print(sum2)
