#!/usr/bin/env python3
# https://adventofcode.com/2024/day/12
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
input = open(filename, "r").read()

W = input.index("\n") + 1
RIGHT = 1
DOWN = 2
LEFT = 4
UP = 8
DIRS = {UP, DOWN, LEFT, RIGHT}

visited = [False] * len(input)
regions = []
perimeters = []

for i, t in enumerate(input):
    if t == "\n":
        continue

    if not visited[i]:
        region = set()
        todo = {i}
        perim = 0
        while len(todo) > 0:
            pos = todo.pop()
            visited[pos] = True
            touching = 0
            border = 0
            if input[pos + 1] != "\n" and input[pos + 1] == t:
                touching += 1
                if not visited[pos + 1]:
                    todo.add(pos + 1)
            else:
                border += RIGHT

            if pos + W < len(input) - 1 and input[pos + W] == t:
                touching += 1
                if not visited[pos + W]:
                    todo.add(pos + W)
            else:
                border += DOWN

            if input[pos - 1] != "\n" and input[pos - 1] == t:
                touching += 1
                if not visited[pos - 1]:
                    todo.add(pos - 1)
            else:
                border += LEFT

            if pos - W >= 0 and input[pos - W] == t:
                touching += 1
                if not visited[pos - W]:
                    todo.add(pos - W)
            else:
                border += UP

            perim += 4 - touching
            region.add((pos, border))

        regions.append(sorted(region))
        perimeters.append(perim)


# TODO improve the execution time by narrowing down the iteration scope to just the range of the input region in both verticals. Still a prettly lame apporach
def sides(region):
    pos, border = zip(*region)
    res = 0
    for dir in DIRS:
        s = ""
        step = W if dir == LEFT or dir == RIGHT else 1
        for c in range(step):
            for i in range(c, len(input), step):
                s += "#" if i in pos and border[pos.index(i)] & dir else " "
        res += len(s.split())
    return res


print(sum(len(region) * perimeters[i] for i, region in enumerate(regions)))
print(sum(len(region) * sides(region) for region in regions))
