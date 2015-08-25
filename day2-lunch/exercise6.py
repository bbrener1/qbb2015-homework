#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015-homework/day2-lunch/SRR072893.sam"
filename = "SRR072893.sam"
f = open(filename)
total = 0
counter = 0

for line in f:
    if not line.startswith("@"):
        total += int(line.split()[4])
        counter += 1

print total/counter

