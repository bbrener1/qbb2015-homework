#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as math

from blaster1 import BLASTER

reader = BLASTER( sys.stdin)

for i in reader:
    print i    
    
scorelist = []
elist = []

reader2 = BLASTER( sys.stdin)

for i in reader2:
    print i[1]
    elist.append(float(i[2]))   

print elist
    
plt.figure()
plt.scatter( math.log(scorelist) , math.log(elist) )
plt.savefig("scoreexpect.png")