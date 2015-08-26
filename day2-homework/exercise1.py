#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment = '#', header = None)
df.columns = ["chromosome","database","type","start","end","score","strand","frame","attributes"]

roi = df["attributes"].str.contains("Sxl")

plt.figure()
plt.title("Sxl")
plt.plot(df[roi]["start"])
plt.ylabel("start position")
plt.xlabel("gene")
plt.savefig("exercise1.png")