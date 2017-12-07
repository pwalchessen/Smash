#!/bin/sh
#SBATCH --job-name=simhash_2-10
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=5
#SBATCH --mail-type=end
#SBATCH --mail-user=yzhan231@jhu.edu

python simhash_dif_2-10mer.py >result_2_10.txt
