#!/usr/bin/env python3
import sys

def algo(values: list[int]):
    for i in range(0, len(values)-2):
        input1 = values[i]

        for j in range(i+1, len(values)-1):
            input2 = values[j]

            for k in range(j+1, len(values)):
                input3 = values[k]

                if input1 + input2 + input3 == 2020:
                    return input1 * input2 * input3


infile = open(sys.argv[1], "r")

lines = infile.readlines();

values = list(map((lambda s: int(s)), lines))

print(algo(values))