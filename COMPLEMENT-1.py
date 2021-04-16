from itertools import islice
comp = {'A':'T','G':'C','C':'G','T':'A','N':'N','R':'Y','Y':'R', \
    'M':'K','K':'M','S':'W','W':'S','H':'D','B':'V','V':'B','D':'H'}
path = r'C:\Users\admin\Desktop\rotation\Python_assignment\caulobacterNA1000.fasta'
dna_seq = []
with open(path,'r') as f1:
    for line in islice(f1, 1, None):
        line=line.strip('\n')
        dna_seq = dna_seq + list(line)
dna_seq = [comp[base] for base in dna_seq]
string = ''.join(dna_seq)
string =string [::-1]
f_new=open(r'C:\Users\admin\Desktop\rotation\Python_assignment\2-NA1000comp2.txt','w')
f_new.write(string)
f_new.close()
