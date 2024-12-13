#!/usr/bin/env python3
# https://adventofcode.com/2024/day/9
import sys

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
input = open(filename, "r").read()

disk = []
part = []
for i in range(len(input) // 2):
    disk += [i] * int(input[i * 2])
    part.append([i, int(input[i * 2])])
    try:
        disk += [None] * int(input[i * 2 + 1])
        part.append([None, int(input[i * 2 + 1])])
    except:
        break


def checksum(disk):
    revc = len(disk) - 1
    i = 0
    while i < len(disk) and i <= revc:
        if disk[i] is None:
            while disk[revc] is None:
                revc -= 1
            disk[i] = disk[revc]
            disk[revc] = None
            revc -= 1
        i += 1

    return sum([i * int(v) for i, v in enumerate(disk) if v is not None])


### part 2
fixed = part.copy()
for y in range(len(input) - 2, -1, -2):
    r = part.index(fixed[y])
    for i in range(1, r, 2):
        d = part[i][1] - part[r][1]
        if d >= 0:
            part[i][1] = d
            try:
                part[r + 1][1] += part[r][1] + part[r - 1][1]
            except:
                pass
            x = part[r]
            part.pop(r)
            part.pop(r - 1)
            part.insert(i, [None, 0])
            part.insert(i + 1, x)
            break

idx = 0
for p in part:
    sum2 += sum([p[0] * (idx + i) for i in range(p[1]) if p[0] is not None])
    idx += p[1]

print(checksum(disk))
print(sum2)
