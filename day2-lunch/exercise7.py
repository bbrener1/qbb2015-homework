#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015-homework/day2-lunch/SRR072893.sam"
filename = "SRR072893.sam"
f = open(filename)
total = 0
counter = 0
row = []
for line in f:
    if not line.startswith("@"):
        row = line.split()
        if row[2]=="2L" and int(row[3]) > 10000 and int(row[3]) <= 20000:
            counter += 1

print counter