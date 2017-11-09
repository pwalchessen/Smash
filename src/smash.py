"""
Created on Thu Nov  2 23:02:44 2017

"""


import re, sys
from simhash import Simhash, SimhashIndex



def version1():
    #reading two genome files
    geno_file_1, geno_file_2, geno_file_3 = open(sys.argv[1]), open(sys.argv[2]), open(sys.argv[3])
    file_1 = geno_file_1.readlines()
    file_2 = geno_file_2.readlines()
    file_3 = geno_file_3.readlines()

    '''
    #reading three genome files from hardcoding handle
    geno_file_1, geno_file_2, geno_file_3 = open('e_coli.fna'), open('s_pom.fna'), open('s_cer.fna')
    file_1, file_2, file_3 = geno_file_1.readlines(), geno_file_2.readlines(), geno_file_3.readlines()
    
    #reading the test files (short genome sequences). test_3.txt is nearly identical to test_2.txt
    geno_file_1, geno_file_2, geno_file_3 = open('test_1.txt'), open('test_2.txt'), open('test_3.txt')
    file_1, file_2, file_3 = geno_file_1.readlines(), geno_file_2.readlines(), geno_file_3.readlines()
    '''
    #take the name line off and keep the sequences which is currently separated by'\n'
    #and then put all sequences together as the input genome
    del file_1[0], file_2[0], file_3[0]
    geno_1, geno_2, geno_3 = '', '', ''

    for i in file_1:
        geno_1 = geno_1 + i.strip()
    for i in file_2:
        geno_2 = geno_2 + i.strip()
    for i in file_3:
        geno_3 = geno_3 + i.strip()

    #geno_1, geno_2 and geno_3 are 3 imported genome sequence strings

    #chop 2 genomes to produce 3-mers
    def get_features(s):
        width = 3
        s = s.lower()
        s = re.sub(r'[^\w]+', '', s)
        return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

    geno_1_kmers = get_features(geno_1)
    geno_2_kmers = get_features(geno_2)
    geno_3_kmers = get_features(geno_3)

    #view simhash_proj value

    geno_1_simh_val = Simhash(geno_1_kmers).value
    geno_2_simh_val = Simhash(geno_2_kmers).value
    geno_3_simh_val = Simhash(geno_3_kmers).value


    #get distance of two simhash_proj

    dis_geno_1_to_2 = Simhash(geno_1).distance(Simhash(geno_2))
    dis_geno_1_to_3 = Simhash(geno_1).distance(Simhash(geno_3))
    dis_geno_2_to_3 = Simhash(geno_2).distance(Simhash(geno_3))

    #simhash_proj 3 genomes
    geno_1_simh = Simhash(geno_1_kmers)
    geno_2_simh = Simhash(geno_2_kmers)
    geno_3_simh = Simhash(geno_3_kmers)

    print("{} {} {}".format(geno_1_simh_val, geno_2_simh_val, geno_3_simh_val))


def read_file(filename):
    with open(filename) as file:
        file_lines = file.readlines()

    file_lines = [l.strip() for l in file_lines]

    return file_lines[1:]


def create_kmer_list(string, kmer_size):
    return [string[i:i + kmer_size] for i in range(0, len(string) - kmer_size + 1, 1)]


def create_kmer_generator(string, kmer_size):
    return (string[i:i + kmer_size] for i in range(0, len(string) - kmer_size + 1, 1))


def list_to_string(l):
    return "".join(l)


def version2():
    scer = read_file("s_cer.fna")
    spom = read_file("s_pom.fna")
    ecoli = read_file("e_coli.fna")

    # scer_string = list_to_string(scer)
    # spom_string = list_to_string(spom)

    # scer_sh = Simhash(scer_string)
    # spom_sh = Simhash(spom_string)

    #scer_kmer = create_kmer_generator(scer_string, 1000000)

    #scer_kmer_simhash = Simhash(scer_kmer)

    scer_simhash = Simhash(scer)
    spom_simhash = Simhash(spom)
    ecoli_simhash = Simhash(ecoli)

    print("S-CER simhash_proj: {}".format(scer_simhash.value))
    print("S-POM simhash_proj: {}".format(spom_simhash.value))
    print("ECOLI simhash_proj: {}".format(ecoli_simhash.value))

    print("S-CER vs. S-POM: {}".format(scer_simhash.distance(spom_simhash)))
    print("S-CER vs. E-COLI: {}".format(scer_simhash.distance(ecoli_simhash)))
    print("S-POM vs. E-COLI: {}".format(spom_simhash.distance(ecoli_simhash)))



if __name__ == '__main__':
    # version1()
    version2()