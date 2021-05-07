import pandas as pd
from itertools import islice
import tempfile

def fastaline(path):
    with open(path,'r') as f1:
        with tempfile.TemporaryFile(mode='r+t') as f2:
            for line in islice(f1, 1, None):
                line=line.strip('\n')
                f2.writelines(line)
            f2.seek(0)
            dna_seq=f2.read()
    return dna_seq

def kmercounter(dna_seq,k):
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
    df = pd.DataFrame.from_dict(kmers, orient='index',columns=['Fre'])
    df = df.reset_index().rename(columns = {'index':'k-num'})
    df.sort_values("Fre",inplace=True,ascending=False)
    df['%'] = df["Fre"] / df["Fre"].sum() * 100
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

def kmersset(dnaline,k):
    S = set()
    i = 0 
    while i <= len(dnaline)-k:
        j = i + k
        di = dnaline[i:j]
        S.add(di)
        i += 1 
        if i > len(dnaline)-k:
            break
    return S
