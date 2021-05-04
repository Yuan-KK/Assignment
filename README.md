This is a *k*-mer counter toolkit that can be used to analyze and compare k-mers produced from genomes. It includes these functions as follows:
- [Count the base number](https://github.com/Yuan-KK/Assignment/blob/main/README.md#1count-the-base-number)
- [Get the complementary strand](https://github.com/Yuan-KK/Assignment/blob/main/README.md#2get-the-complementary-strand)
- [Translate the DNA sequence](https://github.com/Yuan-KK/Assignment/blob/main/README.md#3translate-the-dna-sequence)
- [*K*-mer counter](https://github.com/Yuan-KK/Assignment/blob/main/README.md#4k-mer-counter)
- [Compare genome similarity](https://github.com/Yuan-KK/Assignment/blob/main/README.md#5compare-genome-similarity)
  - [Bray–Curtis dissimilarity](https://github.com/Yuan-KK/Assignment/blob/main/README.md#51-braycurtis-dissimilarity)
  - [MinHash](https://github.com/Yuan-KK/Assignment/blob/main/README.md#52-minhash)
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

[`kmers_counter.py`](https://github.com/Yuan-KK/Assignment/blob/main/kmers_counter.py) is the program to count *k*-mers' species and frequency. 

**Usage:**
```sh
python kmers_counter.py -k <int> -i read.fasta [-o output.csv]
```
The `output.csv` includes three columns, which means *k*-mer, frequency, and percentage.
### *K* = 2
> Count the occurrences of all di-nucleotides.
```sh
$ python kmers_counter.py -k 2 -i ~/python/test/EcoliK12.fasta -o DINULC.csv
```
```sh
$ cat DINULC.csv
k-num,Fre,%
GC,384102,8.275115901647927
CG,346793,7.471328628541871
TT,339584,7.316017511872391
AA,338006,7.282020987790766
CA,325327,7.008863871928329
TG,322379,6.94535198790258
AT,309950,6.677580886628487
CC,271821,5.856127485672662
GG,270252,5.822324858116218
TC,267395,5.760773483400626
GA,267384,5.760536498758739
AC,256773,5.5319324955710805
GT,255699,5.508794176899555
AG,238013,5.127765960861771
CT,236149,5.087607836091081
TA,212024,4.567857428315916
```
### *K* = 3
> Count the occurrences of all tri-nucleotides.
```sh
$ python kmers_counter.py -k 3 -i ~/python/test/EcoliK12.fasta -o TRINULC.csv
```
# 5.Compare genome similarity.
In this part, I use two different standards to quantify the similarity between two genomes.
### 5.1 Bray–Curtis dissimilarity
The Bray–Curtis dissimilarity is a statistic used to quantify the compositional dissimilarity between two different sites, based on counts at each site. The index of dissimilarity is:

![Bray–Curtis dissimilarity](https://gitee.com/yuan-keke/runoob-test/raw/master/20210504185804.jpeg)

[`BC.py`](https://github.com/Yuan-KK/Assignment/blob/main/BC.py) is the program to calculate the compositional dissimilarity between pairs of site.

**Usage:**
```sh
python BC.py -k <int> -i "read1.fasta read2.fasta ..." [-o output.png]
```
### 5.2 MinHash
> MinHash is an approximate algorithm that used to estimate genome distance by calculating Jaccard distances. For detailed principles, please refer to https://blog.csdn.net/liujan511536/article/details/47729721.

**Jaccard distance**
> Jaccard distance is used to describe the dissimilarity between sets. It compares members for two sets to see which members are shared and which are distinct.

![Jaccard distance](https://gitee.com/yuan-keke/runoob-test/raw/master/20210504110402.svg)

[`minhash.py`](https://github.com/Yuan-KK/Assignment/blob/main/minhash.py) is the program to calculate the compositional dissimilarity between pairs of site.
**Usage:**
```sh
python BC.py -k <int> -i "read1.fasta read2.fasta ..." [-o output.png]
```
