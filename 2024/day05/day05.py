#!/usr/bin/env python3
# https://adventofcode.com/2024/day/5

sum1 = 0
sum2 = 0

rule_list, update_list = map(
    lambda x: x.splitlines(), open("input", "r").read().split("\n\n")
)
rules = [tuple(map(int, r.split("|"))) for r in rule_list]
updates = [list(map(int, u.split(","))) for u in update_list]


def swap(u, r):
    a, b = u.index(r[0]), u.index(r[1])
    if a < b:
        u[a], u[b] = u[b], u[a]
        return True
    return False


def recurse(u):
    for a, b in rules:
        if a in u and b in u and swap(u, (a, b)):
            recurse(u)
            break


def is_correct(u):
    return all([u.index(a) < u.index(b) for a, b in rules if a in u and b in u])


status = [is_correct(u) for u in updates]

sum1 = sum([u[len(u) // 2] for u, valid in zip(updates, status) if valid])

incorrect = [u for u, valid in zip(updates, status) if not valid]
for u in incorrect:
    recurse(u)
    sum2 += u[len(u) // 2]


print(sum1)
print(sum2)
