#!/usr/bin/env python3
# https://adventofcode.com/2024/day/24
# https://edotor.net/

import sys
import re
import operator as op
from functools import cache

sum1 = sum2 = 0

filename = sys.argv[1] if len(sys.argv) >= 2 else "input"
data = open(filename, "r").read().split("\n\n")

inputs = {k: int(v) for line in data[0].split("\n") for k, v in [line.split(":")]}
gates = {
    k: v
    for line in data[1].split("\n")
    for *v, k in re.findall(r"(\w+) ([A-Z]+) (\w+) -> (\w+)", line)
}

OPS = {"XOR": op.xor, "AND": op.and_, "OR": op.or_}


@cache
def eval(a, o, b, k=None):
    a = inputs[a] if a in inputs else eval(*gates[a], k=a)
    b = inputs[b] if b in inputs else eval(*gates[b], k=b)
    return OPS[o](a, b)


def number(d=dict(), id=""):
    return sum(v << int(k[1:]) for k, v in d.items() if k.startswith(id))


def swap(candidates):
    for a, b in candidates:
        gates[a], gates[b] = gates[b], gates[a]


# part 1
print(number({k: eval(*v, k=k) for k, v in gates.items() if k.startswith("z")}))


# part 2
def print_conflicts():
    conflicts = set()
    for v in range(len(inputs) // 2):
        x = y = 1 << v
        for i in range(len(inputs) // 2):
            inputs[f"x{i:02}"] = (x >> i) & 1
            inputs[f"y{i:02}"] = (y >> i) & 1

        x = number(inputs, "x")
        y = number(inputs, "y")
        xy = x + y
        res = number({k: eval(*v, k=k) for k, v in gates.items() if k.startswith("z")})

        if res != xy:
            conflicts.add(v)
            k = f"z{v:02}"
            eval(*gates[k], k=k)
            print(v, x, "+", y, "=", xy, res)


def graphviz():
    header = """
graph G {
mode="neato"
"""

    def subgraph(x):
        r = len(inputs) // 2 if x != "z" else len(inputs) // 2 + 1
        pins = ";".join(f"x{i:02}" for i in range(r))
        return [f"subgraph cluster_{x} {{", pins, "}"]

    i = 0
    nodes = []
    for k in sorted(gates):
        a, o, b = gates[k]
        nodes.append(f'{o}{i} [label="{o}" shape=box]')
        nodes.append(f"{a};{b};{k} [shape=plain]")
        nodes.append(f"{{{a} {b}}} -- {o}{i} -- {k}")
        i += 1
    print(header, *subgraph("x"), *subgraph("y"), *subgraph("z"), *nodes, "}", sep="\n")


x = number(inputs, "x")
y = number(inputs, "y")
candidates = [("z12", "vdc"), ("z21", "nhn"), ("z33", "gst"), ("tvb", "khg")]
swap(candidates)
z = number({k: eval(*v, k=k) for k, v in gates.items() if k.startswith("z")})
# print(x + y, z, x + y == z)
print(*sorted(sum(candidates, ())), sep=",")
