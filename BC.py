import pandas as pd
import argparse
from func import fastalist
from func import kmercounter
from func import BCd
parser = argparse.ArgumentParser(usage='python BC.py -k <int> -i "read1.fasta read2.fasta ..." -o output.png')
parser.add_argument("-k","--kmer",type=int,metavar='',required=True,help="Set the length of k-mer")
parser.add_argument("-i","--input",type=str,metavar='',help="Input .fasta file in the form of a string with spaces separating")
parser.add_argument("-o","--output",type=str,metavar='',default='BC.png',help="Output a heatmap")
args = parser.parse_args()
data = args.input.split(' ')
l = len(data)
k = args.kmer
df_dic = {}
alist = []
for i in range(l):
    a = data[i].split('.')[0]
    alist.append(a)
for i in range(l):
    df_dic[alist[i]]=pd.DataFrame(kmercounter(fastalist(data[i]),k))

dfn = pd.merge(df_dic[alist[0]],df_dic[alist[1]],on='k-num',how='outer')
i = 2
while i < l:
    df = pd.merge(dfn,df_dic[alist[i]],on='k-num',how='outer')
    i += 1
df = df.fillna(0)
namelist=alist[:]
namelist.insert(0, 'k-num')
df.columns = namelist
com_dic = {}
for j in alist:
    for k in alist:
        index = j+'|'+k
        d = BCd(df[j],df[k])
        com_dic[index] = d
df_com = pd.DataFrame(com_dic,index = ['value'])
df_com = pd.DataFrame(df_com.values.T, index=df_com.columns, columns=df_com.index)
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
plt.title("Bray–Curtis dissimilarity")
plt.savefig(args.output)
plt.show()
