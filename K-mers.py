import pandas as pd
from itertools import islice

# for a sequence
# dna_seq = list(input("input dnaseq:"))

# for a fasta file
path = input("input path:")
k = int(input("k:")) 
dna_seq = []
with open(path,'r') as f1:
    for line in islice(f1, 1, None):
        line=line.strip('\n')
        dna_seq = dna_seq + list(line)

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
print(fre)
fre = df['Fre'].tolist()
per = []
for f in fre:
    f /= a
    f *= 100
    per.append(f)
df['%'] = per
print(df)
with open(r"C:\Users\admin\Desktop\rotation\Python_assignment\6-knulc.csv",'w+',newline='') as nf:
    df.to_csv(nf,index=False)
