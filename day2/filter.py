#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)
name_counts={}

#Iterate file line by line
for linecount, data in enumerate(f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name] = 1
    else:
        name_counts[gene_name] += 1
for key, value in name_counts.iteritems():
    print key, value