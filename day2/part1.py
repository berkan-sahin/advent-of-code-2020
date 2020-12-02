#!/usr/bin/env python3
import sys

valids = 0
def check_pass(passwd: str, letter: str, letter_range: range, prev_valids: int = valids):
     global valids
     letter_count = 0
     for char in passwd:
         if char == letter:
             letter_count += 1

     if letter_count in letter_range:
         valids += 1

def filter_input(line: str):
    tokens = line.split()
    
    tmp = tokens[0].split("-")
    letter_range = range(int(tmp[0]), int(tmp[1]) + 1)

    passwd = tokens[2]

    letter = tokens[1][0:1]

    return passwd, letter, letter_range

infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

for l in lines:
    p, let ,let_r = filter_input(l)
    check_pass(p, let, let_r)

    
print(valids)