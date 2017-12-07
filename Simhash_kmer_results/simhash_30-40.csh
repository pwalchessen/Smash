#!/bin/sh
#SBATCH --job-name=simhash_30-40
#SBATCH --time=100:00:00
#SBATCH --cpus-per-task=5
#SBATCH --mail-type=end
#SBATCH --mail-user=yzhan231@jhu.edu

python simhash_dif_30-40mer.py >result_30_40.txt
