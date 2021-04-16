# C:\Users\admin\Desktop\rotation\Python_assignment\caulobacterNA1000.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliK12.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliO157.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\Homo sapiens chromosome 21.fasta

from itertools import islice
import pandas as pd

dna_seq = []
k= 3
with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\EcoliO157.fasta','r') as f1:
    for line in islice(f1, 1, None):
        line=line.strip('\n')
        dna_seq = dna_seq + list(line)
k3 = []
i = 0 
while i <= len(dna_seq)-k:
    j = i + k
    di = dna_seq[i:j]
    di = ''.join(di)
    k3.append(di)
    i += 1 
    if i > len(dna_seq)-k:
        break

df = pd.value_counts(k3)
df = pd.DataFrame({'tri-num':df.index, 'Fre':df.values})
print(df)
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
with open(r"C:\Users\admin\Desktop\rotation\Python_assignment\5-O157trinulc.csv",'w+',newline='') as nf:
    df.to_csv(nf,index=False)
