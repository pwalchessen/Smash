#!/usr/bin/env python2
###############################################################################
#----------------------------SCRIPT DESCRIPTION-------------------------------#
###############################################################################
# Script for comparing fasta files with counted k-mers
# Code written by Nathan P. Roach for 601.647 Computational Genomics: Sequences
# Contact info:
# Email 1: nroach2@jhu.edu
# Email 2: natproach@gmail.com
import sys
import numpy
import random
import jellyfish
from scipy.spatial.distance import cosine
from os import listdir
from os.path import isfile, join
if len(sys.argv != 3):
    print "Usage: ./compare_jfs.py /path/to/dir/with/jf/files/ k"
    print "If jellyfish indexes are not built for folder with data, please run smash.sh"
    sys.exit()
k = int(sys.argv[2])
cosineFile = open("%scosinek%d.log" %(sys.argv[1],k),'w')
jaccardFile = open("%sjaccardk%d.log" %(sys.argv[1],k),'w')

#build our list of files / genomes to compare
files = [sys.argv[1]+f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f)) and f.endswith('k%d.jf' %(k))]


#print files
for idx, jfi_1 in enumerate(files[:-1]):
    for jfi_2 in files[idx+1:]:
        jfi1_RFile = jellyfish.ReadMerFile(jfi_1)
        jfi1_QFile = jellyfish.QueryMerFile(jfi_1)
        jfi2_RFile = jellyfish.ReadMerFile(jfi_2)
        jfi2_QFile = jellyfish.QueryMerFile(jfi_2)
        t1 = []
        t2 = []
        notUnion=0
        for mer, count1 in jfi1_RFile:
            #print count1
            count2 = jfi2_QFile[mer]
            if count2 == 0:
                notUnion+=1
            t1.append(int(count1))
            t2.append(int(count2))
        for mer, count2 in jfi2_RFile:
            if jfi1_QFile[mer] == 0:
                t1.append(0)
                t2.append(int(count2))
                notUnion+=1
        log = open('log.txt','w')
        v1 = numpy.zeros(len(t1))
        v2 = numpy.zeros(len(t1))
        for x in range(len(v1)):
            #if t1[x] > 1:
            #    print t1[x]
            v1[x] = float(t1[x])
            v2[x] = float(t2[x])
        #print v1[:100], v2[:100]
        #print v1[-100:], v2[-100:]
        cosineFile.write("%s\t%s\t%f\n" %(jfi_1, jfi_2, 1 - cosine(v1,v2)))
        #print "%s\t%s\t%f" %(jfi_1, jfi_2, 1 - cosine(v1,v2))
        jaccardFile.write("%s\t%s\t%f\n" %(jfi_1, jfi_2, float(len(v1) -\
            notUnion) / float(len(v1))))
        #print "%s\t%s\t%f" %(jfi_1, jfi_2, float(len(v1) - notUnion) \
            #/ float(len(v1)))