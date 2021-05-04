import argparse
parser = argparse.ArgumentParser(usage='python LENGHT.py -i read.fasta')
parser.add_argument("-i","--input",type=str,metavar='',help="Input a .fasta file")
args = parser.parse_args()

f = open (args.input,"r")
base_num = 0
for line in f:
    if ">" not in line :
        line=line.strip('\n')
        base_num += len(line)
print(base_num)
f.close
