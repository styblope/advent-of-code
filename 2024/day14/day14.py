#!/usr/bin/env python3
# https://adventofcode.com/2024/day/14
import sys
import re


filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")
robots = [
    list(map(int, re.findall(r"(-?\d+)", line.strip()))) for line in f.readlines()
]

X, Y = (101, 103) if filename == "input" else (11, 7)


def moveall():
    for i in range(len(robots)):
        robot = robots[i]
        px, py, vx, vy = robot
        robots[i][0] = (px + vx) % X
        robots[i][1] = (py + vy) % Y


def safetyfactor(grid):
    QUADRANTS = {(0, 0), (X // 2 + 1, 0), (0, Y // 2 + 1), (X // 2 + 1, Y // 2 + 1)}
    res = 1
    for qx, qy in QUADRANTS:
        s = sum(sum(grid[qy + y][qx : qx + X // 2]) for y in range(Y//2))

        res *= s
    return res


def fillgrid():
    grid = [[0] * X for _ in range(Y)]
    for robot in robots:
        px, py = robot[0], robot[1]
        grid[py][px] += 1
    return grid


def is_vertical():
    robots.sort()
    prev = robots[0]
    contig = 0
    for robot in robots:
        if robot[0] == prev[0] and robot[1] == prev[1] + 1:
            contig += 1
        prev = robot
        if contig > 100:
            return True


part1 = 0
seconds = 0
while not is_vertical():
    moveall()
    seconds += 1

    if seconds == 100:
        part1 = safetyfactor(fillgrid())

for row in fillgrid():
    print("".join("*" if i > 0 else " " for i in row))

print(part1)
print(seconds)
