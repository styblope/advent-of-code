#!/usr/bin/env python3
# https://adventofcode.com/2024/day/16
# https://www.redblobgames.com/pathfinding/a-star/introduction.html

import sys
from queue import PriorityQueue

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
grid = open(filename, "r").read()

W = grid.index("\n") + 1
start = grid.index("S")
end = grid.index("E")


best_path_tiles = set()
for i in range(0, 1):

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: [start - 1]}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        neighbors = [current + d for d in [1, W, -1, -W] if grid[current + d] != "#"]
        for next in neighbors:
            cost = 1 if next - current == current - came_from[current][-1] else 1001
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost <= cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                if next in came_from:
                    came_from[next].append(current)
                else:
                    came_from[next] = [current]

    if i == 0:
        sum1 = cost_so_far[end]

    for k in range(1000):
        p = end
        while p != start:
            best_path_tiles.add(p)
            if len(came_from[p]) > 1:
                p = came_from[p].pop()
            else:
                p = came_from[p][0]


print(sum1)
print(len(best_path_tiles))
