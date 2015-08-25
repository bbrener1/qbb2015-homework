#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015-homework/day2-lunch/SRR072893.sam"
filename = "SRR072893.sam"
f = open(filename)
diction = {"2L":0,"2R":0,"3L":0,"3R":0,"4":0,"X":0}

for line in f:
    if not line.startswith("@"):
        if line.split()[2] in diction:
            diction[line.split()[2]] = diction[line.split()[2]] + 1

print diction
