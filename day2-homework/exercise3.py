#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

tabulardata = "/Users/cmdb/qbb2015/rawdata/samples.csv"

f = pd.read_csv(tabulardata, index_col=False)
pandas_is_trash = list(f.columns.values)
openstring = ""
weirdvariable = ""

for i in range(0,15):
     weirdvariable = f[pandas_is_trash[0]].irow(i) 
     openstring = "/Users/cmdb/qbb2015/stringtie/" + weirdvariable + "/t_data.ctab"
     g = open(openstring)
     for line in g:
         if "FBtr0331261" in line:
            print line
            