#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

SxlF = []
SxlM = []

for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    SxlF.append(df[roi]["FPKM"].values)
    
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    SxlM.append(df[roi]["FPKM"].values)

plt.figure()
fig, ax = plt.subplots()
plt.plot(SxlF , "b")
plt.plot(SxlM , "r")
ax.set_xticklabels(["10","11","12","13","14A","14B","14C","14D"])
plt.savefig("timecourse.png")

'''
df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

plt.figure()
plt.scatter(df["FPKM"],df2["FPKM"])
plt.xlabel("893 - male 10")
plt.ylabel("195 - female 14")
plt.savefig("Scatter.png")

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
'''