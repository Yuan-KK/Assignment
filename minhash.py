import pandas as pd
import numpy as np
import random
import argparse
from func import fastalist
from func import kmersset

parser = argparse.ArgumentParser(usage='python minhash.py -k <int> -t <int> -i "read1.fasta read2.fasta read3.fasta"')
parser.add_argument("-k","--kmer",type=int,metavar='',default=15,help="Set the length of k-mer")
parser.add_argument("-t","--times",type=int,metavar='',default=100,help="Set the times of running hash function")
parser.add_argument("-i","--input",type=str,metavar='',required=True,help="Input .fasta files in the form of a string with spaces separating")
parser.add_argument("-o","--output",type=str,metavar='',default='JS.png',help="Output a heatmap")
args = parser.parse_args()
data = args.input.split(' ')
l = len(data)
k = args.kmer
S_dic = {}
alist = []
for i in range(l):
    a = data[i].split('.')[0]
    alist.append(a)
for i in range(l):
    S_dic[alist[i]]=kmersset(fastalist(data[i]),k)
u_S = set()
for i in range(l):
    u_S = u_S | S_dic[alist[i]]
u_S = list (u_S)
S = len(u_S)

cha_mat = np.zeros(shape=(S,l), dtype=np.int32)
cha_mat = pd.DataFrame(cha_mat)
cha_mat.columns=alist
cha_mat.index = u_S
for i in u_S:
    j = 0 
    while j < l:
        if i in S_dic[alist[j]]:
            cha_mat.at[i,alist[j]] = 1
        else:
            cha_mat.at[i,alist[j]] = 0
        j += 1
print(cha_mat)

h_mat = np.zeros(shape=(S,args.times), dtype=np.int32)
h_times = ["h" + str(num1) for num1 in range(args.times)]
h_mat = pd.DataFrame(h_mat,columns= h_times)
h = [x for x in range(S)]   
for i in h_times:
    random.shuffle(h)
    h_mat[i] = h 
h_mat.index = u_S

sign_mat =[np.inf for i in range(l)]
sign_mat = [sign_mat] * args.times 
sign_mat = pd.DataFrame(sign_mat,index = h_times,columns= alist)
for i in u_S:
    num = list(cha_mat.loc[i])
    t= []
    for x,y in enumerate(num):
        if y == 1:
            t.append( x )
    for u in t:
        t1 = sign_mat[alist[u]]
        t2 = h_mat.loc[i]
        for n in range(len(t1)):
            if t2[n]<=t1[n]:
                t1[n]=t2[n]
        sign_mat[alist[u]] = t1
print('Signature_matrix',sign_mat)


dic = {}
for x in alist:
    for y in alist:
        i = 0
        C = []
        Str = x + '|' + y       
        count = 0
        count0 = 0
        while i < args.times:
            if sign_mat[x][i] == sign_mat[y][i] and sign_mat[x][i] != 0:
                count += 1
            if sign_mat[x][i] == sign_mat[y][i] and sign_mat[x][i] == 0:
                count0 += 1 
            i += 1
        D = count/(len(sign_mat[x])-count0)
        dic[Str] = D

df_com = pd.DataFrame(dic,index = ['value'])
df_com = pd.DataFrame(df_com.values.T, index=df_com.columns, columns=df_com.index)
print(df_com)
df_com["index"]=df_com.index
df_com['A'] = df_com['index'].str.split('|',expand=True)[0]
df_com['B'] = df_com['index'].str.split('|',expand=True)[1]
df_com = df_com.pivot(index = 'A',columns='B',values='value')

if __name__ == '__main__':
    print(df_com)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(dpi=120)
sns.heatmap(data=df_com,annot=True, linewidths=.5,
            cmap=sns.diverging_palette(10, 220, sep=80, n=7))
plt.title("Jaccard Similarity")
plt.savefig(args.output)
plt.show()
