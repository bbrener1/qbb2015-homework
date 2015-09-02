#!/usr/bin/env python

import chromebits
import sys
import matplotlib.pyplot as plt

A = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])
B = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])
C = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])
D = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])
E = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])

A.set_bits_from_file(sys.argv[2])
B.set_bits_from_file(sys.argv[3])
C.set_bits_from_file(sys.argv[4])


D = A.intersect(B.complement())

E = A.union(B.union(C))

    
varA = len(A.intersect(E).intervals())
varB = len(B.intersect(E).intervals())
varC = len(C.intersect(E).intervals())
varAB = len (A.intersect(B.intersect(E)).intervals())
varAC = len (A.intersect(C.intersect(E)).intervals())
varBC = len (B.intersect(C.intersect(E)).intervals())
varABC = len (A.intersect(B.intersect(C.intersect(E))).intervals())

plt.figure()
pltv.venn3(subsets = [varA,varB,varAB,varC,varAC,varBC,varABC])
plt.savefig("venn2.png")
