#!/usr/bin/env python3
import sys

valids = 0
def check_pass(passwd: str, letter: str, min_pos: int, max_pos: int, prev_valids: int = valids):
    global valids
    letter_count = 0
    in_min_pos = False
    in_max_pos = False
    for i, char in enumerate(passwd):
        if i == min_pos - 1:
            in_min_pos = char == letter
        elif i == max_pos - 1:
            in_max_pos = char == letter

    if (in_max_pos or in_min_pos) and not (in_max_pos and in_min_pos):
        valids += 1
        

def filter_input(line: str):
    tokens = line.split()
    
    tmp = tokens[0].split("-")
    min_p = int(tmp[0])
    max_p = int(tmp[1])

    passwd = tokens[2]

    letter = tokens[1][0:1]

    return passwd, letter, min_p, max_p

infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

for l in lines:
    p, let, min_p, max_p = filter_input(l)
    check_pass(p, let, min_p, max_p)

    
print(valids)