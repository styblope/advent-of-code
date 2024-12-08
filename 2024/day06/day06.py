#!/usr/bin/env python3

NONE = 0
UP = 1
RIGHT = 2
DOWN = 4
LEFT = 8

with open("input", "r") as f:
    input = f.read()

start = input.index("^")
W = input.index("\n") + 1
len_input = len(input)
OFFSETS = {UP: -W, RIGHT: 1, DOWN: W, LEFT: -1}
NEXT_DIR = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}


def walk(p, d, obstruction=None):
    global visited, path
    visited = [0] * len_input
    path = []

    while True:
        if visited[p] & d:
            return True

        visited[p] |= d
        path.append((p, d))

        next = p + OFFSETS[d]

        # check bounds
        if next < 0 or next >= len_input or input[next] == "\n":
            return False

        # check obstacle
        if input[next] == "#" or next == obstruction:
            d = NEXT_DIR[d]
        else:
            p = next


# part 1
path = [0] * 10000  # global list of (position, direction) tuples
visited = [0] * len_input  # global array of visited directions
walk(start, UP)
sum1 = sum(1 for v in visited if v)

# part 2
obstacles = [i for i, v in enumerate(visited) if v and i != start]
p, d = zip(*path)
sum2 = 0
for o in obstacles:
    idx = p.index(o)
    sum2 += walk(p[idx - 1], d[idx - 1], obstruction=o)

print(sum1, sum2)
