#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as mat 

df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
roi = df[df["FPKM"]!=0]["FPKM"]
roi = mat.log(roi)

plt.figure()
roi.plot(kind='kde')
plt.savefig("kde.png")