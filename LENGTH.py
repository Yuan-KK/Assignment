# C:\Users\admin\Desktop\rotation\Python_assignment\caulobacterNA1000.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliK12.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\EcoliO157.fasta
# C:\Users\admin\Desktop\rotation\Python_assignment\Homo sapiens chromosome 21.fasta

PATH = r"C:\Users\admin\Desktop\rotation\Python_assignment\Homo sapiens chromosome 21.fasta"
f = open (PATH,"r")
base_num = 0
for line in f:
    if ">" not in line :
        line=line.strip('\n')
        base_num += len(line)
print(base_num)
f.close
