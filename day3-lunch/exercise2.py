#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as mat 

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
output = df[df["FPKM"] != 0]["FPKM"]

print output
plt.figure()
plt.hist(mat.log(output.values))
plt.savefig("exercise2.png")


"""
chromosomes = {}

for i, line in df.iterrows():
    #print line["chr"]
    if line["chr"] in ["2L","2R","3L","3R","X","Y"]:
        if line["chr"] not in chromosomes:
            chromosomes[line["chr"]] = 1
        else:
            chromosomes[line["chr"]] += 1
    

chromosomes.values()
        
plt.figure()
plt.bar(range(len(chromosomes)), chromosomes.values())
plt.savefig("barplot.png")
#print chromosomes
"""