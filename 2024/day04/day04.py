#!/usr/bin/env python3


input = open("input", "r").read()
W = input.index("\n") + 1
sum1 = 0
sum2 = 0


def is_match(pos, inc, x=False):
    for x in "XMAS" if x else "MAS":
        if pos < 0 or pos >= len(input):
            return False
        if input[pos] != x:
            return False
        pos += inc

    return True


for p in range(len(input)):
    sum1 += sum(
        is_match(p, d, x=True) for d in {-1, 1, -W, W, -W - 1, W + 1, -W + 1, W - 1}
    )

    sum2 += sum(
        [
            is_match(p, W + 1) and is_match(p + 2, W - 1),
            is_match(p + 2, W - 1) and is_match(p + 2 + W + W, -W - 1),
            is_match(p + 2 + W + W, -W - 1) and is_match(p + W + W, -W + 1),
            is_match(p + W + W, -W + 1) and is_match(p, W + 1),
        ]
    )

print(sum1)
print(sum2)
