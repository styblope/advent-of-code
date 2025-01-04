#!/usr/bin/env python3
# https://adventofcode.com/2024/day/9
import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
input = open(filename, "r").read()

disk = []
part = []
fs = []
pos = 0
for id in range(len(input) // 2):
    disk += [id] * int(input[id * 2])
    part.append([id, int(input[id * 2])])
    try:
        disk += [None] * int(input[id * 2 + 1])
        part.append([None, int(input[id * 2 + 1])])

        # [id, position, length]
        len_block = input[id*2]
        len_space = input[id*2 + 1]
        fs.append([id, pos, len_block])
        pos = len_block + len_space 
    except:
        break


def checksum(disk):
    i = 0
    k = len(disk) - 1
    while i < len(disk) and i <= k:
        if disk[i] is None:
            while disk[k] is None:
                k -= 1
            disk[i] = disk[k]
            disk[k] = None
            k -= 1
        i += 1

    return sum([i * int(v) for i, v in enumerate(disk) if v is not None])


# part 2
fixed = part.copy()
for y in range(len(input) - 2, -1, -2):
    r = part.index(fixed[y])
    for id in range(1, r, 2):
        d = part[id][1] - part[r][1]
        if d >= 0:
            part[id][1] = d
            try:
                part[r + 1][1] += part[r][1] + part[r - 1][1]
            except:
                pass
            x = part[r]
            part.pop(r)
            part.pop(r - 1)
            part.insert(id, [None, 0])
            part.insert(id + 1, x)
            break

idx = 0
for p in part:
    sum2 += sum([p[0] * (idx + i) for i in range(p[1]) if p[0] is not None])
    idx += p[1]

print(checksum(disk))
print(sum2)
