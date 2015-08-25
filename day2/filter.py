#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)
linecount = 0

for data in f:
    if linecount < 10:
        pass
    elif linecount <=15:
        print data
    else:
        break
    linecount += 1
    