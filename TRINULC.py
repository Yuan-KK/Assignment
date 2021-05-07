# C:\Users\admin\Desktop\rotation\Python_assignment\caulobacterNA1000.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliK12.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliO157.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\Homo sapiens chromosome 21.fasta

from itertools import islice
import pandas as pd
import tempfile

k= 3
with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\EcoliO157.fasta','r') as f1:
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
    tri = dna_seq[i:j]
    if tri not in kmers.keys():
        kmers[tri] = 1
    if tri in kmers.keys():
        kmers[tri] += 1
    i += 1 
    if i > len(dna_seq)-k:
        break

df = pd.DataFrame([kmers])
df = pd.DataFrame.from_dict(kmers, orient='index',columns=['Fre'])
df = df.reset_index().rename(columns = {'index':'k-num'})
df.sort_values("Fre",inplace=True,ascending=False)
df['%'] = df["Fre"] / df["Fre"].sum() * 100
with open(r"C:\Users\admin\Desktop\rotation\Python_assignment\tri-O157trinulc.csv",'w+',newline='') as nf:
    df.to_csv(nf,index=False)
