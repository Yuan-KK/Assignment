import pandas as pd
from itertools import islice
import tempfile
import argparse

parser = argparse.ArgumentParser(usage='python kmers_counter.py -k <int> -i read.fasta [-o output.csv]')
parser.add_argument("-k","--kmer",type=int,metavar='',required=True,help="Set the length of k-mer")
parser .add_argument("-i","--input",type=str,metavar='',required=True,help="Input .fasta file")
parser.add_argument("-o","--output",type=str,metavar='',default='output.csv',help="Output .csv file")
args = parser.parse_args()

k = args.kmer
with open(args.input,'r') as f1:
    with tempfile.TemporaryFile(mode='r+t') as f2:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            f2.writelines(line)
        f2.seek(0)
        line=f2.read()
        dna_seq = list(line)

kmers = []
i = 0 
while i <= len(dna_seq)-k:
    j = i + k
    di = dna_seq[i:j]
    di = ''.join(di)
    kmers.append(di)
    i += 1 
    if i > len(dna_seq)-k:
        break

df = pd.value_counts(kmers)
df = pd.DataFrame({'k-num':df.index, 'Fre':df.values})

fre = df['Fre'].tolist()
a = 0 
for i in fre:
    a += i
fre = df['Fre'].tolist()
per = []
for f in fre:
    f /= a
    f *= 100
    per.append(f)
df['%'] = per

with open(args.output,'w+',newline='') as nf:
    df.to_csv(nf,index=False)
