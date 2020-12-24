#!/usr/bin/env python

import sys

assert(len(sys.argv) >= 2)

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

current_state = set()


def move(pos, op):
    if op == "e":
        return (pos[0]+2, pos[1])
    elif op == "se":
        return (pos[0]+1, pos[1]-1)
    elif op == "ne":
        return (pos[0]+1, pos[1]+1)
    elif op == "w":
        return (pos[0]-2, pos[1])
    elif op == "nw":
        return (pos[0]-1, pos[1]+1)
    elif op == "sw":
        return (pos[0]-1, pos[1]-1)
    else:
        sys.exit(f"fatal: unknown {op}")


for cur in lines:
    pos = (0, 0)
    exp = ""
    for c in cur:
        exp += c
        if c in ["e", "w"]:
            pos = move(pos, exp)
            exp = ""
    if pos in current_state:
        current_state.remove(pos)
    else:
        current_state.add(pos)

print(f"part 1: {len(current_state)}")


def n_neighbors(coords, h):
    val = 0
    for n in [(-2, 0), (2, 0), (-1,-1), (-1, 1), (1, -1), (1, 1)]:
        v = (h[0] + n[0], h[1] + n[1])
        if v in coords:
            val += 1
    return val


for i in range(100):
    next_state = set()
    for c in current_state:
        for neigh in [(0, 0), (-2, 0), (2, 0), (-1,-1), (-1, 1), (1, -1), (1, 1)]:
            h = (c[0] + neigh[0], c[1] + neigh[1])
            cnt = n_neighbors(current_state, h)
            add_next = h in current_state
            if h not in current_state and cnt == 2:
                add_next = True
            elif h in current_state and (cnt == 0 or cnt > 2):
                add_next = False
            if add_next:
                next_state.add(h)
    current_state = next_state

print(f"part 2: {len(current_state)}")
