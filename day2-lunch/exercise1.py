#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015-homework/day2-lunch/SRR072893.sam"
filename = "SRR072893.sam"
f = open(filename)
counter = 0
for line in f:
    if not line.startswith("@"):
        counter += 1

print counter
