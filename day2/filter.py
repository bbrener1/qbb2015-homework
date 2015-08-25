#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)

for data in f:
    if "tRNA" in data.split()[9]:
        print data,