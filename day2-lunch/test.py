#!/usr/bin/env python

counter = 0

f = open( "SRR072893.sam" )
for line in f:
    counter += 1

print counter
