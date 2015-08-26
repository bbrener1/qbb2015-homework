#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment = '#', header = None)
df.columns = ["chromosome","database","type","start","end","score","strand","frame","attributes"]

roi = df["attributes"].str.contains("Sxl")
roi2 = df["type"].str.contains("transcript")

roif = roi & roi2

plt.figure()
plt.title("Sxl/transcripts")
plt.plot(df[roif]["start"])
plt.ylabel("start position")
plt.xlabel("gene")
plt.savefig("exercise2.png")
