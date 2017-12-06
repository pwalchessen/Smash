package main

import (
	"fmt"
	"smash/src/simhash"
	"io/ioutil"
	"strings"
)

func get_genome_string(filename string) string {
	data, _ := ioutil.ReadFile(filename)
	data_string := strings.Split(strings.TrimSpace(string(data)), "\r\n")
	genome_strings := data_string[1:]

	return strings.Join(genome_strings[:],"")
}


func main() {
	s_cer := get_genome_string("../resources/S_cer.fna")
	s_pom := get_genome_string("../resources/S_pom.fna")
	e_coli := get_genome_string("../resources/e_coli.fna")

	var docs = [][]byte{
		[]byte(s_cer),
		[]byte(s_pom),
		[]byte(e_coli),
	}


	hashes := make([]uint64, len(docs))
	for i, d := range docs {
		hashes[i] = simhash.Simhash(simhash.NewWordFeatureSet(d))
		fmt.Printf("Simhash of %v: %x\n", i, hashes[i])
	}

	fmt.Printf("Comparison of 1 and 2: %d\n", simhash.Compare(hashes[0], hashes[1]))
	fmt.Printf("Comparison of 1 and 3: %d\n", simhash.Compare(hashes[0], hashes[2]))
	fmt.Printf("Comparison of 2 and 3: %d\n", simhash.Compare(hashes[1], hashes[2]))
}
