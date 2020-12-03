#!/usr/bin/env python3
import sys

TREE = "#"

def traverse(b_map: list[str]):
    x_length = len(b_map[0]) - 1
    y_length = len(b_map)
    x = 0
    trees = 0

    for y in range(0, y_length):
        if b_map[y][x] == TREE:
            trees += 1
        
        x = (x + 3) % x_length

    return trees


infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()
print(traverse(lines))