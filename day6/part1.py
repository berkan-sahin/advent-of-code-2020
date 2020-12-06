#!/usr/bin/env python3
import sys

def questions_person(answers: str, yes_list: list):
    for ans in answers:
        yes_list[ord(ans) - ord("a")] = True

    return yes_list


def questions_group(grp_answers):
    yes_list = [False for i in range(0, 26)]
    pos_answers = 0
    if type(grp_answers) == str:
        grp_answers = grp_answers[:-1]
        yes_list = questions_person(grp_answers, yes_list)
    
    elif type(grp_answers) == list:
        for person in grp_answers:
            person = person[:-1]
            yes_list = questions_person(person, yes_list)
    
    for q in yes_list:
        pos_answers += (1 if q else 0)
    
    return pos_answers



infile = open(sys.argv[1], "r")
lines = infile.readlines()
infile.close()

lines.append("\n")
current_group = []
sum = 0
for ln in lines:
    if ln == "\n":
        sum += questions_group(current_group)
        current_group = []
    else:
        current_group.append(ln)

print(sum)