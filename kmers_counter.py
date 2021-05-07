from numpy import ERR_DEFAULT
import pandas as pd
from itertools import islice
import tempfile
import argparse

parser = argparse.ArgumentParser(usage='python kmers_counter.py -k <int> -i read.fasta -o output.csv')
parser.add_argument("-k","--kmer",type=int,metavar='',required=True,help="Set the length of k-mer")
parser .add_argument("-i","--input",type=str,metavar='',required=True,help="Input a .fasta file")
parser.add_argument("-o","--output",type=str,metavar='',default='output.csv',help="Output a .csv file")
# parser.add_argument("--hist",type=str,metavar='',default='hist.png',help="Output a histogram")
args = parser.parse_args()

k = args.kmer
with open(args.input,'r') as f1:
    with tempfile.TemporaryFile(mode='r+t') as f2:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            f2.writelines(line)
        f2.seek(0)
        dna_seq=f2.read()

kmers = { }
i = 0 
while i <= len(dna_seq)-k:
    j = i + k
    di = dna_seq[i:j]
    if di not in kmers.keys():
        kmers[di] = 1
    if di in kmers.keys():
        kmers[di] += 1
    i += 1 
    if i > len(dna_seq)-k:
        break

df = pd.DataFrame([kmers])
df = pd.DataFrame(df.values.T, index=df.columns, columns=['Fre'])
df.sort_values("Fre",inplace=True,ascending=False)
df['%'] = df["Fre"] / df["Fre"].sum() * 100

with open(args.output,'w+',newline='') as nf:
    df.to_csv(nf,index=False)
