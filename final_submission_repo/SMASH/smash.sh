#!/usr/bin/env bash

###############################################################################
#----------------------------SCRIPT DESCRIPTION-------------------------------#
###############################################################################
# Script for comparing fasta files by counted k-mers
# Generates Jellyfish indexes then calls compare function
# Requires installation of Jellyfish - https://github.com/gmarcais/Jellyfish
# Requires installation of Jellyfish Python wrapper https://github.com/gmarcais/Jellyfish/tree/master/swig
# Code written by Nathan P. Roach for 601.647 Computational Genomics: Sequences Final Project
# Contact info:
# Email 1: nroach2@jhu.edu
# Email 2: natproach@gmail.com
if [ -z ${4+x} ] #test if we have enough of out inputs
then
    echo "Usage: ./smash.sh /path/to/dir/with/fasta/files/ k #_of_kmers #_of_threads"
    echo "Dependencies:"
	echo "\tjellyfish - https://github.com/gmarcais/Jellyfish"
	echo "\thttps://github.com/gmarcais/Jellyfish/tree/master/swig"
else
	startDir=$(pwd)
	cd ${1}
	#for entry in ${1}*.fa ${1}*.fna ${1}*.fasta
	for entry in *.fa *.fna *.fasta
	do
		[ -f "$entry" ] || break
		echo "Starting kmer-count of ${entry}"
		# some weird idiosyncracy with jellyfish, doesn't output counts if output
		# file is explicitly specified or if file specified is in another directory.
		# have to make the counts then move them to output we want.
		jellyfish count -m ${2} -s ${3} -t ${4} -C ${entry}
		echo "Done with kmer-count of ${entry}"
		mv "mer_counts.jf" "${entry}.k${2}.jf"
	done
	cd ${startDir}
	./compare_jfs.py ${1} ${2}
fi
