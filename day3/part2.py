#!/usr/bin/env python3
import sys

TREE = "#"

def traverse(b_map: list[str], r: int, d: int):
    x_length = len(b_map[0]) - 1
    y_length = len(b_map)
    x = 0
    trees = 0

    for y in range(0, y_length, d):
        if b_map[y][x] == TREE:
            trees += 1
        
        x = (x + r) % x_length

    return trees


infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

a = traverse(lines, 1, 1)
b = traverse(lines, 3, 1)
c = traverse(lines, 5, 1)
d = traverse(lines, 7, 1)
e = traverse(lines, 1, 2)
print(a * b * c * d * e)