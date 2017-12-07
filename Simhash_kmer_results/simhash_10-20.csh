#!/bin/sh
#SBATCH --job-name=simhash_10-20
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=5
#SBATCH --mail-type=end
#SBATCH --mail-user=yzhan231@jhu.edu

python simhash_dif_10-20mer.py >result_10_20.txt
