#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd

inputfile = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"


file = pd.read_table(inputfile, comment = '#')

column = file[file["FPKM"]!= 0]

sortedcol = column.sort("FPKM")

bottom = sortedcol[0:int(sortedcol.shape[0]/3)]
middle = sortedcol[sortedcol.shape[0]/3:int(sortedcol.shape[0]*.666)]
top = sortedcol[int(sortedcol.shape[0]*.666):]

plt.figure()
bottom.boxplot("FPKM")
plt.savefig("exercise4a.png")
middle.boxplot("FPKM")
plt.savefig("exercise4b.png")
top.boxplot("FPKM")
plt.savefig("exercise4c.png")
