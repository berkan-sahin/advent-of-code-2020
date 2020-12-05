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

for i in range(0, 927):
    eq1 = False
    eq2 = False
    eq3 = False
    for s_id in seat_ids:
        if i == s_id:
            eq1 = True
            break
        
    for s_id in seat_ids:
        if i-1 == s_id:
            eq2 = True
            break
    
    for s_id in seat_ids:
        if i+1 == s_id:
            eq3 = True
            break

    if (not eq1) and eq2 and eq3:
        print(i) 
