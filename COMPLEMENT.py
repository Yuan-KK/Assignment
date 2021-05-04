from itertools import islice
import tempfile
import argparse
comp = {'A':'T','G':'C','C':'G','T':'A','N':'N','R':'Y','Y':'R', \
    'M':'K','K':'M','S':'W','W':'S','H':'D','B':'V','V':'B','D':'H'}
parser = argparse.ArgumentParser(usage='python COMPLEMENT.py -i read.fasta [-o output.txt]')
parser.add_argument("-i","--input",type=str,metavar='',required=True,help="Input a .fasta file")
parser.add_argument("-o","--output",type=str,metavar='',default='output.txt',help="Output a .txt file")
args = parser.parse_args()
with open(args.input,'r') as f1:
    with tempfile.TemporaryFile(mode='r+t') as f2:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            f2.writelines(line)
        f2.seek(0)
        line=f2.read()
        dna_seq = list(line)
        dna_seq = [comp[base] for base in dna_seq]
        string = ''.join(dna_seq)
        string =string [::-1]
        f_new=open(args.output,'w')
        f_new.write(string)
        f_new.close()
