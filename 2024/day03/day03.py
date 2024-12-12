#!/usr/bin/env python3
# https://adventofcode.com/2024/day/3
import re


def sum_mul(s):
    return sum(
        int(m.group(1)) * int(m.group(2))
        for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", s)
    )


input = open("input", "r").read()
part2 = re.sub(r"don\'t\(\).*?do\(\)|don\'t\(\).*", "", input, flags=re.S)

print(sum_mul(input))
print(sum_mul(part2))
