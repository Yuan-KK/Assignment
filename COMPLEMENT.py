from itertools import islice

with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\caulobacterNA1000.fasta','r') as f1:
    with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\2-NA1000.txt','w') as f2:
        for line in islice(f1, 1, None):
            line=line.strip('\n')
            f2.writelines(line)

f=open(r'C:\Users\admin\Desktop\rotation\Python_assignment\2-NA1000.txt','r')
line=f.read()
transline=line[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
f.close()

f_new=open(r'C:\Users\admin\Desktop\rotation\Python_assignment\2-NA1000comp.txt','w')
f_new.write(transline)
f_new.close()
