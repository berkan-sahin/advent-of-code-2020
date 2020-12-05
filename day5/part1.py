#!/usr/bin/env python3
import sys

def seat_id(bpass: str) -> int:
    row_str = bpass[:7]
    col_str = bpass[7:-1]

    p = 2**6
    acc_row = 0
    for c in row_str:
        acc_row += (0 if c == "F" else p)
        p /= 2

    p = 2**2
    acc_col = 0
    for c in col_str:
        acc_col += (0 if c == "L" else p)
        p /= 2
    return acc_row * 8 + acc_col


infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

seat_ids = list(map(seat_id, lines))

seat_ids.sort()
print(seat_ids[len(seat_ids) - 1])