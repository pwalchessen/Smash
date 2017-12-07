#!/bin/sh
#SBATCH --job-name=simhash_20-30
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=5
#SBATCH --mail-type=end
#SBATCH --mail-user=yzhan231@jhu.edu

python simhash_dif_20-30mer.py >result_20_30.txt
