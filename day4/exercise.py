#!/usr/bin/env python

"""
Boris Brenerman, Johns Hopkins, QBB2015
Count Intersection of two BED files

Incomplete code
"""

from __future__ import division
import numpy 
import sys
import matplotlib.pyplot as plt
import matplotlib_venn as pltv

arrProt = []


def arrays_from_len_file ( fname ):
    arrays = {}
    for line in open (fname):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name] = numpy.zeros(size, dtype=bool)
    return arrays
    

def set_bits_from_file ( arrays, fname ):
    for line in open ( fname ):
        fields = line.split()
        #parse fields
        chrom = fields[0]
        start = int ( fields [1] )
        end = int ( fields [2])
        arrays[chrom][start:end] = 1



def unique_regions(file):
    uniques = 0
    doubles = 0
    triples = 0
    total = 0
    for line in open (file):
        tempUniqueCount=0
        fields = line.split()
        #parse fields
        chrom = fields[0]
        start = int ( fields [1] )
        end = int ( fields [2])
        #get slice
        for arrays in arrProt:
            sl = arrays[chrom][start:end]    
            if True in sl:
                tempUniqueCount += 1
        if (1 == tempUniqueCount):
            uniques += 1
    return uniques

def pairwise (file1, file2, len):
    doubles = 0
    total = 0
    file2Array = arrays_from_len_file(len)
    set_bits_from_file(file2Array,file2)    
    for line in open (file1):
        fields = line.split()
        #parse fields
        chrom = fields[0]
        start = int ( fields [1] )
        end = int ( fields [2])
        #get slice
        sl = file2Array[chrom][start:end]    
        if sl.any():
            doubles += 1
        total += 1
    return doubles
    
def threeway (file):
    triples = 0
    total = 0
    for line in open (file):
        tempUniqueCount=0
        fields = line.split()
        #parse fields
        chrom = fields[0]
        start = int ( fields [1] )
        end = int ( fields [2])
        #get slice
        for arrays in arrProt:
            sl = arrays[chrom][start:end]    
            if sl.any():
                tempUniqueCount += 1
        if (3 == tempUniqueCount):
            triples += 1
        total += 1
    return triples



##FILLS ARRPLOT FROM EARLIER WITH FILE ORDERED ARRAYS

for file in sys.argv[2:]:
    arraystemp = arrays_from_len_file(sys.argv[1])
    set_bits_from_file (arraystemp, file )
    arrProt.append(arraystemp)    



varA = int(unique_regions(sys.argv[2]))
varB = int(unique_regions(sys.argv[3]))
varC = int(unique_regions(sys.argv[4]))

varAB = int(pairwise(sys.argv[2],sys.argv[3],sys.argv[1])+pairwise(sys.argv[3],sys.argv[2],sys.argv[1])-threeway(sys.argv[2])-threeway(sys.argv[3]))
varBC = int(pairwise(sys.argv[3],sys.argv[4],sys.argv[1])+pairwise(sys.argv[4],sys.argv[3],sys.argv[1])-threeway(sys.argv[3])-threeway(sys.argv[4]))
varAC = int(pairwise(sys.argv[2],sys.argv[4],sys.argv[1])+pairwise(sys.argv[4],sys.argv[2],sys.argv[1])-threeway(sys.argv[2])-threeway(sys.argv[4]))

varABC = int(threeway(sys.argv[2])+threeway(sys.argv[3])+threeway(sys.argv[4]))

print [varA,varB,varAB,varC,varAC,varABC]
plt.figure()
pltv.venn3(subsets = [varA,varB,varAB,varC,varAC,varBC,varABC])
plt.savefig("venn2.png")

""""
total = 0
any_overlap = 0
all_overlap = 0
half_overlap = 0
arrays = arrays_from_len_file(sys.argv[1])

set_bits_from_file (arrays, sys.argv[2])
for line in open (sys.argv[3]):
    fields = line.split()
    #parse fields
    chrom = fields[0]
    start = int ( fields [1] )
    end = int ( fields [2])
    #get slice
    sl = arrays[chrom][start:end]
    total += 1
    any_overlap += sl.any()
    all_overlap += sl.all()
    half_overlap += (numpy.sum(sl)/len(sl) > .5)

print "Total: %d, any overlap: %d, all overlap: %d, half overlap: %d" %(total, any_overlap, all_overlap, half_overlap)
    """
#for key, value in arrays.iteritems():
#    print key, type (value), value.shape, numpy.sum(value)
