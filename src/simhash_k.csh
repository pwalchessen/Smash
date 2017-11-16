#!/bin/sh
#SBATCH --job-name= simhash_k_size
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=5
#SBATCH --mail-type=end
#SBATCH --mail-user=yzhan231@jhu.edu
ml python

python simhash_dif_kmer.py >result_k_size.txt
