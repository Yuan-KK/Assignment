PATH = input("input path:")
f = open (PATH,"r")
base_num = 0
for line in f:
    if ">" not in line :
        line=line.strip('\n')
        base_num += len(line)
print(base_num)
f.close
