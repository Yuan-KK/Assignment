from itertools import islice
import tempfile
import argparse
codon = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'stop', 'TAG':'stop',
    'TGC':'C', 'TGT':'C', 'TGA':'stop', 'TGG':'W'}

parser = argparse.ArgumentParser(usage='python TRANSLATE.py -i read.fasta [-o output.fasta]')
parser .add_argument("-i","--input",type=str,metavar='',required=True,help="Input a .fasta file")
parser.add_argument("-o","--output",type=str,metavar='',default='output.fasta',help="Output a .fasta file")
args = parser.parse_args()


with open(args.input,'r') as f1:
    with tempfile.TemporaryFile(mode='r+t') as f2:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            f2.writelines(line)
        f2.seek(0)
        dna_seq=f2.read()
        
k= 3
kmers = []
start = []
i = 0 
while i <= len(dna_seq)-k:
    j = i + k
    di = dna_seq[i:j]
    kmers.append(di)
    if di == 'ATG':
        start.append(i)
    i += 1

aa = []
stratsite = []
for l in start:
    while l <= len(dna_seq)-k:
        n = l + k
        tri = dna_seq[l:n]
        l = l + 3 
        for key,value in codon.items():
            tri= tri.replace(key,value)
        aa.append(tri)
        if tri == 'stop' or l > len(dna_seq)-k:
            aa.append('\n')
            break
aa = ''.join(aa)
aalist = aa.split('\n') 
aalist = aalist[:-1]
pro_df={"startsite" : start,
   "pro" : aalist}
with open(args.output,'w+',newline='') as f:
    for i in range(len(start)):
        f.write('>startsite '+str(start[i])+'\n'+aalist[i]+'\n')
