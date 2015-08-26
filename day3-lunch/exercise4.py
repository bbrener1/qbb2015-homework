#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as mat 

df1 = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

r = df1["FPKM"] + 1
g = df2["FPKM"] + 1

m = mat.log(r/g)

a = .5 * mat.log(r * g)

plt.figure()
plt.scatter(a,m)
plt.savefig("MA.png")