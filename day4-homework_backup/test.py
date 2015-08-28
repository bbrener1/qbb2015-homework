#!/usr/bin/env python

import chromebits
import sys

A = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])
B = chromebits.ChromosomeLocationBitArrays(fname=sys.argv[1])

A.set_bits_from_file(sys.argv[2])
B.set_bits_from_file(sys.argv[3])

C = A.intersect(B.complement())

print C.intervals()