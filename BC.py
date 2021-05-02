import pandas as pd
from itertools import islice
import os
import argparse
parser = argparse.ArgumentParser(usage='python BC.py -k <int> -i "read1.fasta read2.fasta read3.fasta"')
parser.add_argument("-k","--kmer",type=int,metavar='',required=True,help="Set the length of k-mer")
parser.add_argument("-i","--input",type=str,metavar='',help="Input .fasta file in the form of a string with spaces separating")
args = parser.parse_args()
data = args.input.split(' ')
l = len(data)
def fastalist(path):
    dna_seq = []
    with open(path,'r') as f1:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            dna_seq = dna_seq + list(line)
    return path,dna_seq

def kmercounter(path,dna_seq):
    kmers = []
    i = 0 
    while i <= len(dna_seq)-args.kmer:
        j = i + args.kmer
        kmer = dna_seq[i:j]
        kmer = ''.join(kmer)
        kmers.append(kmer)
        i += 1 
        if i > len(dna_seq)-args.kmer:
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
    a = os.path.basename(path).split('.')[0]
    df[a] = per
    df.drop('Fre', axis=1,inplace = True)
    return df,a

def BCd(list1,list2):
    C = 0
    sum1 = sum(list1)
    sum2 = sum(list2)
    for i in range(len(list1)):
        min(list1[i],list2[i])
        C += min(list1[i],list2[i])
    dissimilarity = 1 - 2 * C / ( sum1 + sum2 )
    return dissimilarity

df_dic = {}
for i in range(l):
    df_dic[kmercounter(fastalist(data[i])[0],fastalist(data[i])[1])[1]]=pd.DataFrame(kmercounter(fastalist(data[i])[0],fastalist(data[i])[1])[0])
print(df_dic)

dfn = pd.merge(df_dic[kmercounter(fastalist(data[0])[0],fastalist(data[0])[1])[1]],df_dic[kmercounter(fastalist(data[1])[0],fastalist(data[1])[1])[1]],on='k-num',how='outer')
print(dfn)
i = 2
while i < l:
    df = pd.merge(dfn,df_dic[kmercounter(fastalist(data[i])[0],fastalist(data[i])[1])[1]],on='k-num',how='outer')
    i += 1

namelist=list(df_dic.keys())
print(namelist)
com_dic = {}
for j in namelist:
    for k in namelist:
        index = j+'|'+k
        d = BCd(df[j],df[k])
        com_dic[index] = d

df_com = pd.DataFrame([com_dic])
df_com = pd.DataFrame(df_com.values.T, index=df_com.columns, columns=df_com.index)
df_com["index"]=df_com.index
df_com.columns = ['value','index']
df_com['A'] = df_com['index'].str.split('|',expand=True)[0]
df_com['B'] = df_com['index'].str.split('|',expand=True)[1]
df_com = df_com.pivot(index = 'A',columns='B',values='value')
if __name__ == '__main__':
    print(df_com)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(dpi=120)
sns.heatmap(data=df_com,
            cmap=sns.diverging_palette(10, 220, sep=80, n=7))
plt.title("Bray–Curtis dissimilarity")
plt.savefig('./BCd.jpg')
plt.show()
