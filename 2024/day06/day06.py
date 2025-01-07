#!/usr/bin/env python3
# https://adventofcode.com/2024/day/7
import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
data = open(filename, "r").read()

S = data.index("^")
W = data.index("\n") + 1
len_input = len(data)
UP, RIGHT, DOWN, LEFT = -W, 1, W, -1
NEXT_DIR = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
jumps = dict()


def walk(p, d, obstruction=None):
    visited = dict()
    fr, steps = p, 0
    while True:
        if visited.get(p) == d:
            return visited, True

        if p not in visited:
            visited[p] = d

        next = p + d

        if next < 0 or next >= len_input or data[next] == "\n":
            return visited, False

        if data[next] == "#" or next == obstruction:
            nextd = NEXT_DIR[d]
            if not obstruction:
                jumps[(fr, d)] = steps
                fr, steps = p, 0
            elif (
                (s := jumps.get((p, nextd)))
                and obstruction % W != p % W
                and obstruction // W != p // W
            ):
                p += s * nextd
            d = nextd

        else:
            p = next
            steps += 1


# part 1
visited, _ = walk(S, UP)
print(len(visited))

# part 2
p, d = zip(*visited.items())
sum2 = sum(walk(p[i - 1], d[i - 1], obstruction=o)[1] for i, o in enumerate(visited))
print(sum2)
