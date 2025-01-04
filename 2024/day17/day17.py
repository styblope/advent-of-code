#!/usr/bin/env python3
# https://adventofcode.com/2024/day/17

import sys

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
f = open(filename, "r")

a = 55593699
b = 0
c = 0

data = list(map(int, "2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0".split(",")))
dl = len(data)


def combo(o):
    match o:
        case o if 0 <= o <= 3:
            return o
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case _:
            return 0


def prog():
    global a, b, c, data
    output = []
    ptr = 0
    while ptr < dl:
        if ptr + 1 >= dl:
            break
        operand = data[ptr + 1]
        match data[ptr]:
            case 0:
                a //= 2 ** combo(operand)
            case 1:
                b ^= operand
            case 2:
                b = combo(operand) % 8
            case 3:
                ptr = operand if a != 0 else ptr + 1
                continue
            case 4:
                b ^= c
            case 5:
                output.append(combo(operand) % 8)
            case 6:
                b = a // 2 ** combo(operand)
            case 7:
                c = a // 2 ** combo(operand)
        ptr += 2
    return output


print(*prog(), sep=",")

oc = i = 0
increment = 2 ** (3 * (dl - 1))
while True:
    a = i
    output = prog()
    if output == data:
        break

    if dl == len(output) and data[-oc - 1 :] == output[-oc - 1 :]:
        increment = 2 ** (3 * (dl - 1 - oc - 1))
        oc += 1

    i += increment

print(i)

