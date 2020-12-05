#!/usr/bin/env python3
import sys
import re

def validate_field(p_line):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    tokens = p_line.split()
    for tok in tokens:
        field_name = tok.split(":")[0]
        field_value = tok.split(":")[1] 

        if field_name == "byr":
            year = int(field_value)
            byr = True if year <= 2002 and year >= 1920 else False

        elif field_name == "hcl":
            hcl = False if re.match("^#[0-f]{6}$", field_value) is None else True

        elif field_name == "iyr":
            year = int(field_value)
            iyr = True if year <= 2020 and year >= 2010 else False

        elif field_name == "eyr":
            year = int(field_value)
            eyr = True if year >= 2020 and year <= 2030 else False

        elif field_name == "hgt":
            unit = field_value[-2:]
            if unit == "cm":
                val = int(field_value[:-2])
                hgt = True if val >= 150 and val <= 193 else False
            elif unit == "in":
                val = int(field_value[:-2])
                hgt = True if val >= 59 and val <= 76 else False
        
        elif field_name == "ecl":
            ecl = False if re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", field_value) is None else True

        elif field_name ==  "pid":
            pid = False if re.match("^[0-9]{9}$", field_value) is None else True
    return byr, iyr, eyr, hgt, hcl, ecl, pid


def validate_pass(p_port) -> bool:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    if type(p_port) == str:
        byr, iyr, eyr, hgt, hcl, ecl, pid = validate_field(p_port)

    elif type(p_port) == list:
        for ln in p_port:
            byr_r, iyr_r, eyr_r, hgt_r, hcl_r, ecl_r, pid_r = validate_field(ln)
            byr = byr or byr_r
            iyr = iyr or iyr_r
            eyr = eyr or eyr_r
            hgt = hgt or hgt_r
            hcl = hcl or hcl_r
            ecl = ecl or ecl_r
            pid = pid or pid_r

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
