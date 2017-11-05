#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:02:44 2017

"""
#in case you don't have simhash package in you computer, please install simhash
#first: type in "pip install simhash" in terminal
import re
from simhash import Simhash, SimhashIndex


'''
#reading two genome files
geno_file_1, geno_file_2 = open(sys.argv[1]), open(sys.argv[2], open(sys.argv[3]))
file_1 = geno_file_1.readlines()
file_2 = geno_file_2.readlines()
file_3 = geno_file_3.readlines()
'''

#reading three genome files from hardcoding handle
geno_file_1, geno_file_2, geno_file_3 = open('e_coli.fna'), open('s_pom.fna'), open('s.cer.fna')
file_1, file_2, file_3 = geno_file_1.readlines(), geno_file_2.readlines(), geno_file_3.readlines()

#take the name line off and keep the sequences which is currently separated by'\n'
#and then put all sequences together as the input genome
del file_1[0], file_2[0], file_3[0]
geno_1, geno_2, geno_3 = '', '', ''

for i in file_1:
    geno_1 = geno_1 + i.strip()
for i in file_2:
    geno_2 = geno_2 + i.strip()
for i in file_3:
    geno_3 = geno_3 + i.strip()

#geno_1, geno_2 and geno_3 are 3 imported genome sequence strings

#chop 2 genomes to produce 3-mers    
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

geno_1_kmers = get_features(geno_1)
geno_2_kmers = get_features(geno_2)
geno_3_kmers = get_features(geno_3)

#view simhash value

geno_1_simh_val = Simhash(geno_1_kmers).value
geno_2_simh_val = Simhash(geno_2_kmers).value
geno_3_simh_val = Simhash(geno_3_kmers).value
#get dostance of two simhash

dis_geno_1_to_2 = Simhash(geno_1).distance(Simhash(geno_2))
dis_geno_1_to_3 = Simhash(geno_1).distance(Simhash(geno_3))
dis_geno_2_to_3 = Simhash(geno_2).distance(Simhash(geno_3))

print geno_1_simh_val, ' ', geno_2_simh_val, ' ', geno_3_simh_val

print dis_geno_1_to_2, ' ', dis_geno_1_to_3, ' ',dis_geno_2_to_3