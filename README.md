This is a *k*-mer counter toolkit that can be used to analyze and compare k-mers produced from genomes. It includes these functions as follows:
- [Count the base number](https://github.com/Yuan-KK/Assignment/blob/main/README.md#1count-the-base-number)
- [Get the complementary strand](https://github.com/Yuan-KK/Assignment/blob/main/README.md#2get-the-complementary-strand)
- [Translate the DNA sequence](https://github.com/Yuan-KK/Assignment/blob/main/README.md#3translate-the-dna-sequence)
- [*K*-mer counter](https://github.com/Yuan-KK/Assignment/blob/main/README.md#4k-mer-counter)
- [Compare genome similarity](https://github.com/Yuan-KK/Assignment/blob/main/README.md#5compare-genome-similarity)
  - [Bray–Curtis dissimilarity](https://github.com/Yuan-KK/Assignment/blob/main/README.md#braycurtis-dissimilarity)
  - [MinHash](https://github.com/Yuan-KK/Assignment/blob/main/README.md#minhash)
# 1.Count the base number.
[`Length.py`](https://github.com/Yuan-KK/Assignment/blob/main/LENGTH.py) is the program to count how many DNA bases in a `.fasta` file.

**Usage:**
```sh
python LENGHT.py -i read.fasta
```
**Example:**
```sh
$ python LENGTH.py -i ~/python/test/EcoliK12.fasta 
4641652
```
# 2.Get the complementary strand.
`COMPLEMENT.py` is the program to output the complementary strand of the DNA sequence.

**Usage:**
```sh
python COMPLEMENT.py -i read.fasta [-o output.txt]
```
# 3.Translate the DNA sequence.
`TRANSLATE.py` is the program to translate a DNA sequence to a protein sequence using the standard codon table.

**Usage:**
```sh
python TRANSLATE.py -i read.fasta [-o output.fasta]
```
The `output.fasta` shows all the possible results of translating DNA chains into polypeptide chains.
# 4.*K*-mer counter
*K*-mers are substrings of length *k* contained within a biological sequence. *K*-mers analysis is ubiquitous in biological sequence analysis and is among the first steps of processing pipelines for a wide spectrum of applications, including de novo assembly, error correction, repeat detection, genome comparison, digital normalization, RNA-seq quantification, metagenomic reads classification and binning, fast search-by-sequence over large high-throughput sequencing repositories.

[`kmers_counter.py`](https://github.com/Yuan-KK/Assignment/blob/main/kmers_counter.py)

**Usage:**
```
python kmers_counter.py -k <int> -i read.fasta [-o output.csv]
```
### *K* = 2
> Count the occurrences of all di-nucleotides.
```
python kmers_counter.py -k 2 -i read.fasta -o DINULC.csv
```
### *K* = 3
> Count the occurrences of all tri-nucleotides.
```
python kmers_counter.py -k 3 -i read.fasta -o TRINULC.csv
```
# 5.Compare genome similarity.
### Bray–Curtis dissimilarity
The Bray–Curtis dissimilarity is a statistic used to quantify the compositional dissimilarity between two different sites, based on counts at each site. The index of dissimilarity is:

![Bray–Curtis dissimilarity](https://gitee.com/yuan-keke/runoob-test/raw/master/20210504185804.jpeg)

[`BC.py`](https://github.com/Yuan-KK/Assignment/blob/main/BC.py) is the program to calculate the compositional dissimilarity between pairs of site.

**Usage:**
```
python BC.py -k <int> -i "read1.fasta read2.fasta ..." [-o output.png]
```
### MinHash
> MinHash is an approximate algorithm that used to estimate genome distance by calculating presence-based distances.

**Jaccard distance**
> Jaccard distance is used to describe the dissimilarity between sets.

![Jaccard distance](https://gitee.com/yuan-keke/runoob-test/raw/master/20210504110402.svg)
