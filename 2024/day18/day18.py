#!/usr/bin/env python3
# https://adventofcode.com/2024/day/18
# https://www.redblobgames.com/pathfinding/a-star/introduction.html

import sys
from queue import Queue

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
pos = [complex(*map(int, line.strip().split(","))) for line in open(filename, "r")]

E = 70 if filename == "input" else 6
END = E + 1j * E
shortest_path = []


def bfs(start, end, pos):
    global shortest_path
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    dist = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        neighbors = filter(
            lambda n: n not in pos and 0 <= n.real <= E and 0 <= n.imag <= E,
            [current + d for d in {-1, 1, 1j, -1j}],
        )

        for next in neighbors:
            if next not in came_from:
                frontier.put(next)
                dist[next] = dist[current] + 1
                came_from[next] = current

    shortest_path.clear()
    p = end
    while p != start:
        p = came_from.get(p, start)
        shortest_path.append(p)

    return dist.get(end)


print(bfs(0, END, pos[:1024]))

shortest_path = []
for p in range(len(pos)):
    if shortest_path and pos[p] not in shortest_path:
        continue

    if not (dist := bfs(0, END, pos[1 : p + 1])):
        print(f"\r\033[K{int(pos[p].real)},{int(pos[p].imag)}")
        break
    else:
        print('.', end='', flush=True)
