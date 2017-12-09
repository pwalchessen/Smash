simhash_dif_kmer.py utilized simhash.py to calculate the simhash distance between S.cer and S.pomb, and between S.cer and E.coli at kmer size from 2 to 38 at the interval of 2. The input is the 3 fna files and their path has been hard coded in the script. The output is the distance at different kmer size, which is stored in the output dir.

The get_feature(), Simhash().distance(Simhash()), Simhash().value functions in the simhash_dif_kmer.py is copied from https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
 
To run simhash_dif_kmer.py, please use:

python simhash_dif_kmer.py > result.txt
