import pandas as pd
from itertools import islice
import tempfile

def fastalist(path):
    with open(path,'r') as f1:
        with tempfile.TemporaryFile(mode='r+t') as f2:
            for line in islice(f1, 1, None):
                line=line.strip('\n')
                f2.writelines(line)
            f2.seek(0)
            line=f2.read()
            dna_seq = list(line)
    return dna_seq

def kmercounter(dna_seq,k):
    kmers = []
    i = 0 
    while i <= len(dna_seq)-k:
        j = i + k
        kmer = dna_seq[i:j]
        kmer = ''.join(kmer)
        kmers.append(kmer)
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
    df.drop('Fre', axis=1,inplace = True)
    return df

def BCd(list1,list2):
    C = 0
    sum1 = sum(list1)
    sum2 = sum(list2)
    for i in range(len(list1)):
        min(list1[i],list2[i])
        C += min(list1[i],list2[i])
    dissimilarity = 1 - 2 * C / ( sum1 + sum2 )
    return dissimilarity

def kmersset(dnalist,k):
    S = set()
    i = 0 
    while i <= len(dnalist)-k:
        j = i + k
        di = dnalist[i:j]
        di = ''.join(di)
        S.add(di)
        i += 1 
        if i > len(dnalist)-k:
            break
    return S
