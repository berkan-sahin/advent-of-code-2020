#!/usr/bin/env python3
import sys
import re

def validate_pass(p_port) -> bool:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    cid = True
    if type(p_port) == str:
        tokens = p_port.split()
        for tok in tokens:
            field_name = tok.split(":")[0]
            byr = (field_name == "byr") or byr
            iyr = (field_name == "iyr") or iyr
            eyr = (field_name == "eyr") or eyr
            hgt = (field_name == "hgt") or hgt
            hcl = (field_name == "hcl") or hcl
            ecl = (field_name == "ecl") or ecl
            pid = (field_name == "pid") or pid

    elif type(p_port) == list:
        for ln in p_port:
            tokens = ln.split()
            for tok in tokens:
                field_name = tok.split(":")[0]
                byr = (field_name == "byr") or byr
                iyr = (field_name == "iyr") or iyr
                eyr = (field_name == "eyr") or eyr
                hgt = (field_name == "hgt") or hgt
                hcl = (field_name == "hcl") or hcl
                ecl = (field_name == "ecl") or ecl
                pid = (field_name == "pid") or pid

    return byr and iyr and eyr and hgt and hcl and ecl and pid


infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

lines.append("\n")
current_pass = []
valid_passes = 0
for ln in lines:
    if ln == "\n":
        valid_passes += (1 if validate_pass(current_pass) else 0)
        current_pass = []
    else:
        current_pass.append(ln)

print(valid_passes)
