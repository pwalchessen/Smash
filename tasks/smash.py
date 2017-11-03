#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:02:44 2017

"""
#in case you don't have simhash package in you computer, please install simhash
#first: type in "pip install simhash" in terminal
import re
from simhash import Simhash


'''
#reading two genome files
geno_file_1, geno_file_2 = open(sys.argv[1]), open(sys.argv[2])
file_1 = geno_file_1.readlines()
file_2 = geno_file_2.readlines()
'''

#reading two genome files from hardcoding handle
geno_file_1, geno_file_2 = open('e_coli.fna'), open('s_pom.fna')
file_1, file_2 = geno_file_1.readlines(), geno_file_2.readlines()

#take the name line off and keep the sequences which is currently separated by'\n'
#and then put all sequences together as the input genome
del file_1[0], file_2[0]
geno_1, geno_2 = '', ''
geno_pieces_1, geno_pieces_2 = [], []

for i in file_1:
    geno_1 = geno_1 + i.strip()
for i in file_2:
    geno_2 = geno_2 + i.strip()

#geno_1 and geno_2 are two imported genome sequence strings
    
