# smash_README.md
## Last updated December 8th, 2017 by Nathan Roach

Description of code written by Nathan Roach for JHU class EN.601.647 - Computational Genomics: Sequences Final project
Contact info:
Email 1: nroach2@jhu.edu
Email 2: natproach@gmail.com

smash is a nucleotide sequence comparison algorithm. It counts the k-mers in a set of fasta files, then compares the k-mers between fasta files. It does this both by calculating a jaccard index (indicating the fraction of k-mers present in both files), and by calculating the cosine similarity between the files two k-mer count vectors.
This is done in two steps, first by counting k-mers with the jellyfish algorithm (in smash.sh) ( https://github.com/gmarcais/Jellyfish ) then by reading the resulting k-mer count files with a jellyfish  python module ( in compare\_jfs.py ) ( https://github.com/gmarcais/Jellyfish/tree/master/swig ) and calculating the metrics listed above. As a result both jellyfish and its python module are required for smash's use

To run smash, move all fasta files you wish to compare to a single directory, then call the k-mer counting function with
`./smash.sh /path/to/dir/with/fastas/ k S t`

Where k is the k-mer size to use in the comparison, S is the approximate number of k-mers you expect the k-mer counting algorithm to encounter (note that this is for speed only, as jellyfish will expand its memory usage if the number of k-mers is exceeded ), and t is the number of CPU threads that will be used by jellyfish.
`./smash.sh` automatically calls the compare_jfs.py algorithm, however if you have jellyfish k-mer count files pre-generated you can call this compare script separately with
`./compare_jfs.py /path/to/dir/with/k-mer_count_files/ k`

Where k is the k used in generating the k-mer count files, and the k-mer count files within the specified directory have the file suffix ".k${k}.jf" ( where k is literal and ${k} is the value stored by the k provided)

smash.sh will count the k-mers in the provided fasta files and store the results in a jellyfish file format
compare\_jfs.py will compare each resulting jellyfish formatted files to all the other files, and output the results in two logs jaccardk${k}.log and cosinek${k}.log, storing the jaccard and cosine similarities respectively. These log files are formatted as tab deliminated files with one line per comparison in the following format:
/path/to/fastafile1.fa    /path/to/fastafile2.fa    ComparisonResult