#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment = '#', header = None)

#print df
#print df.head()

#print df.describe()
#print df.info()

#print df[1:5]

#print df.info()
df.columns = ["chromosome","database","type","start","end","score","strand","frame","attributes"]
#print df.info()
#print df.sort("type")

#print df[["chromosome", "start", "end"]]

#print df["start"][9:15]

#print df.shape
#df2 = df["start"]
#print df2.shape

#df2.to_csv("startColumn.txt", sep='\t', index = False)

roi = df["start"] < 10
print df[roi]

