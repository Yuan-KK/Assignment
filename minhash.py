import os
import pandas as pd
from itertools import islice
from pandas import Series, DataFrame
import numpy as np
import random

k = 21
def dnalist(path):
    dna_seq = []
    with open(path,'r') as f1:
        for line in islice(f1, 1, None):
            line=line.strip('/n')
            dna_seq = dna_seq + list(line)
    print(dna_seq[:100])
    return(dna_seq)
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
    print(kmersset)
    return(S)

dna1 = dnalist(r'/public/home/ykk/python/minhash/caulobacterNA1000.fasta')
dna2 = dnalist(r'/public/home/ykk/python/minhash/EcoliK12.fasta')
dna3 = dnalist(r'/public/home/ykk/python/minhash/EcoliO157.fasta')
dna4 = dnalist(r'/public/home/ykk/python/minhash/Homo sapiens chromosome 21.fasta')
S1 = kmersset(dna1,k)
S2 = kmersset(dna2,k)
S3 = kmersset(dna3,k)
S4 = kmersset(dna4,k)
u_S = S1 | S2| S3| S4
u_S = list (u_S)
S = len(u_S)


cha_mat = np.zeros(shape=(S,4), dtype=np.int32)
cha_mat = DataFrame(cha_mat)
col = ['S1','S2','S3','S4']
cha_mat.columns=col
cha_mat.index = u_S
for i in u_S:
    if i in S1:
        cha_mat.at[i,'S1'] = 1
    else:
        cha_mat.at[i,'S1'] = 0
    if i in S2:
        cha_mat.at[i,'S2'] = 1
    else:
        cha_mat.at[i,'S2'] = 0
    if i in S3:
        cha_mat.at[i,'S3'] = 1
    else:
        cha_mat.at[i,'S3'] = 0 
    if i in S4:
        cha_mat.at[i,'S4'] = 1
    else:
        cha_mat.at[i,'S4'] = 0
print(cha_mat)

h_mat = np.zeros(shape=(S,1000), dtype=np.int32)  
h_times = ["h" + str(num1) for num1 in range(1000)] 
h_mat = DataFrame(h_mat,columns= h_times)
h = [x for x in range(S)]   
for i in h_times:
    random.shuffle(h)
    h_mat[i] = h 
h_mat.index = u_S
print(h_mat)

sign_mat =[np.inf for i in range(4)]  
sign_mat = [sign_mat] *1000 
sign_mat = DataFrame(sign_mat,index = h_times,columns= col)
for i in u_S:
    num = list(cha_mat.loc[i])
    t= []
    for x,y in enumerate(num):
        if y == 1:
            t.append( x )
    for u in t:
        t1 = sign_mat[col[u]]
        t2 = h_mat.loc[i]
        for n in range(len(t1)):
            if t2[n]<=t1[n]:
                t1[n]=t2[n]
        sign_mat[col[u]] = t1
print(sign_mat)
with open(r"/public/home/ykk/python/minhash/minhash.csv",'w+',newline='') as nf:
    sign_mat.to_csv(nf,index=False)
