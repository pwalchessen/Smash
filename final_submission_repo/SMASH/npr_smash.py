#!/usr/bin/env python2

###############################################################################
#-----------------------------SCRIPT DESCRIPTION------------------------------#
###############################################################################
# Compares 2 fasta files based on cosine similarity of k-mer counts
# Code written by Nathan P. Roach for 601.647 Computational Genomics: Sequences
# Contact info:
# Email 1: nroach2@jhu.edu
# Email 2: natproach@gmail.com

import sys
import string
import math
import numpy
import random
import jellyfish
from Bio import Seq
from Bio.Alphabet import generic_dna
from scipy.spatial.distance import cosine

def updateDict(num):
    global k_merDict
###############################################################################
#-----------------------------FUNCTION DESCRIPTION----------------------------#
###############################################################################
# Increments counter for current k_mer
    seq = str(k_mer)
    if seq in k_merDict:
        k_merDict[seq][num] += 1
    else:
        if num == 0:
            k_merDict[seq] = [1,0]
        else:
            k_merDict[seq] = [0,1]
 
global k_merDict
k_merDict = {}
global k_mer
k_mer = Seq.MutableSeq('',generic_dna)

sequence1_file = open(sys.argv[1])
sequence2_file = open(sys.argv[2])
k = int(sys.argv[3])
newSeqFlag = True
prevSeq = ''
for fileNum, sequence_file in enumerate((sequence1_file,sequence2_file)):
    for line in sequence_file:
        line = string.strip(line) #remove any white space
        line = string.upper(line) #convert to uppercase
        if line[0] == '>': #Ignore sequence Ids for now
            newSeqFlag = True
            continue
        else:
            if newSeqFlag:
                newSeqFlag = False
                prevSeq = ''
                if k < len(line):
                    start = k
                else:
                    start = len(line)
            else:
                if k < len(line):
                    start = k
                else:
                    start = len(line)
                for x in range(start):
                    k_mer[:] = prevSeq[-k+1+x:]+line[:x+1]
                    updateDict(fileNum)
                    k_mer.reverse_complement()
                    updateDict(fileNum)
            for x in range(start,len(line)):
                k_mer[:] = line[x-k:x]
                updateDict(fileNum)
                k_mer.reverse_complement()
                updateDict(fileNum)
                
            prevSeq = line[-k:]
    sequence_file.close()
    print 'Done with file %d' %(fileNum+1)

numKmers = int(math.ceil(float(sys.argv[4])*len(k_merDict)))
for y in range(int(sys.argv[5])):
    v1 = numpy.zeros(numKmers)
    v2 = numpy.zeros(numKmers)
    sampledVals = random.sample(k_merDict,numKmers)
    notUnion = 0
    for x, key in enumerate(sampledVals):
        v1[x], v2[x] = k_merDict[key]
        if v1[x] == 0 or v2[x] == 0:
            notUnion += 1
             
    print "Cosine Iteration %d: %f" %(y+1, 1 - cosine(v1,v2))
    print "Jaccard Iteration %d: %f" %(y+1, float(numKmers - notUnion) / float(numKmers) )
    