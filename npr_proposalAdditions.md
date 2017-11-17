Base Text:
Final Project Proposal

Nathan Roach, Patricia Walchessen, Charlie Wang, and Yue Zhang

October 26, 2017

Research Topic

A common problem in Computer Science and Bioinformatics is to evaluate the similarity between high dimensionality data in a computationally efficient manner. This is a necessary useful In bioinformatics this problem takes the form of determining the  SimHash is a widely used Locality Sensing Hashing (LSH) algorithm used to determine cosine similarity in large data sets[1]. In 2016, Ondov et al. used MinHash, another LSH algorithm, to analyze the resemblance between genomes and metagenomes[3]. This suggests that SimHash could also be used to analyze the resemblance between genomes and metagenomes.

We would like to implement the SimHash algorithm to determine genetic similarity. Implementation of SimHash would be a slightly different approach as MinHash analyzes resemblance whereas SimHash analyzes cosine similarity, but could prove scientifically useful as cosine similarity is more readily understood in scientific circles. In a paper comparing the results of MinHash vs. SimHash, MinHash outperformed SimHash when data was binary in areas of low and high similarity[2]. Ideally, we will run a comparison of MinHash and SimHash on the same genetic data-sets and determine the optimal algorithm to run for genome similarity. To evaluate our results, we will use the same criteria as Ondov et al. to facilitate comparison.

1
Input Data
1. S. cerevisiae
2. S. pombe
3. E. coli
Milestones
1. Replicating MinHash Data
2. Implementing SimHash algorithm
3. Benchmarking MinHash vs SimHash
Stretch Goals
1. Expand to full genome or multiple full genomes with varying GC content,
redundancy etc.
2. Determine optimal k
References
[1] Caitlin Sadowski and Greg Levin. SimHash: Hash-based Similarity Detection.
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.473.7179&rep
=rep1&type=pdf, 2007.
[2] Anshumali Shrivastava and Ping Li. In Defense of MinHash Over
SimHash. Journal of Machine Learning, 33, 2014.
[3] Brian D. Ondov, Todd J. Treangen, P´all Melsted, Adam B. Mallonee,
Nicholas H. Bergman, Sergey Koren and Adam M. Phillippy. Mash: fast
genome and metagenome distance estimation using MinHash. Genome
Biology, 17:132, 2016.