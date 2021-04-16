# 有100(i)条随机的序列，寻找motif(L bp)  # 假如序列长度不相等
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
L = 7
with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\Gibbs.fasta','r') as f1:
    with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\9-Gibbs.txt','w') as f2:
        for line in f1:
            if 'A' in line:
                line=line.strip('\n')
            f2.writelines(line)
linelist = []
with open(r'C:\Users\admin\Desktop\rotation\Python_assignment\9-Gibbs.txt','r') as f:
    for line in f:
        if '>' not in line:
            linelist.append(line)
for n in range(len(linelist)) :
    if linelist[n].endswith('\n'):
        linelist[n]=linelist[n][:-1]
# 给每条序列编号
dna_seq = {'seq':linelist}
df1 = pd.DataFrame(dna_seq)
# 计算最短序列长
lenlist = []
for x in range(len(df1['seq'])):
    lenlist.append(len(df1['seq'][x]))
short = min(lenlist)
# 计算序列条数
seqsum = df1.shape[0]
# 在每一条序列中随机取L bp的seqcut,生成一个dataframe = df
# 可以生成把起始位点生成lists
i = 0
slist = []
while 1:
    s = random.randint(0,short-L)  # 右边界为最短序列的长-L
    i += 1
    slist.append(s)
    if i == 100 :
        break

seqcutlist = []
for e in range(len(slist)):
    b = slist[e]
    h = df1['seq'][e]
    d = list(h)[b:b+L]
    seqcutlist.append(d)
df2 = pd.DataFrame(seqcutlist)

# 定义函数计算matrix
def cutsample(df,seqcount):  # 输入df = 序列数据框, seqcount = 序列数    
    i = 0 
    countlist = []
    while i < L:
        pera = (list(df[i]).count('A')+1) / (seqcount + 4)   # 拉普拉斯修正
        perc = (list(df[i]).count('C')+1) / (seqcount + 4)
        perg = (list(df[i]).count('G')+1) / (seqcount + 4)
        pert = (list(df[i]).count('T')+1) / (seqcount + 4)
        countlist.append([pera,perc,perg,pert])
        i = i+1
        if i == L:
            break
    countlist = np.asarray(countlist).T
    return countlist
# 计算Frobenius距离
def FrobeniusDistance(A,B):
    A = np.array(A)
    B = np.array(B)
    C = np.mat(A)-np.mat(B)
    # print(C)
    CT = C.transpose()
    vecProd = np.dot(C,CT)
    # print(vecProd)
    F2 = 0
    vecProd = np.array(vecProd)
    for i in range(len(vecProd)):
        F2+=(vecProd[i][i])*(vecProd[i][i])
    F = np.sqrt(F2)
    return(F)
# 输出list最大值索引list中的一个任意值
def mutimaxindex(nums):
    max_of_nums = max(nums)
    # print(max_of_nums)
    # ([k for k, v in count.items() if v == highest])
    # 先把索引和元素写成元组
    tup = [(i, nums[i]) for i in range(len(nums))]
    maxlist = [i for i, n in tup if n == max_of_nums]
    a = random.choice(maxlist)
    return(a)
# 输出连续值的次数
def continue_num(lst):
    length = len(lst)
    total_num = []
    j = 1
    for i in range(length - 1):
        if lst[i] == lst[i+1]:
            j += 1
        else:
            total_num.append(j)
            j = 1
    total_num.append(j)
    fremax = max(total_num)
    return(fremax)

lastmatrix = cutsample(df2,seqsum)
EDdict = {0:1}
u = 1
ulist = []
Flist = []
us = [0, 0]
tests = [0, 0]
continue_0_num = []
i = 0
while 1:    
    df_S = list(df1.loc[i])
    df_S = list(df_S[0])
    df_new = df2.drop([i], 0)
    xmatrix = cutsample(df_new,seqcount = seqsum-1)   
    # 根据xmatrix计算df_S每个kmers的得分
        #提取序列的kmers
    k = L
    kmers = []
    m = 0 
    while m <= len(df_S)-k:
        n = m + k
        di = df_S[m:n]
        di = ''.join(di)
        kmers.append(di)
        m += 1 
        if m > len(df_S)-k:
            break
    x = 0 
    y = 0
    scorelist = []
    for x in range(len(kmers)) :
        allscore = 1
        for y in range(0,L):
            if list(kmers[x])[y] == 'A':   
                score = xmatrix[0,y]
            elif list(kmers[x])[y] == 'C':
                score = xmatrix[1,y]
            elif list(kmers[x])[y] == 'G':
                score = xmatrix[2,y]
            elif list(kmers[x])[y] == 'T':
                score = xmatrix[3,y]
            y += 1
            allscore *= score
        scorelist.append(allscore) 
        x += 1
    maxindex = mutimaxindex(scorelist) 
    df2.loc[i] = list(df1['seq'][i])[maxindex:maxindex+L]
    newmatrix = cutsample(df2,seqsum)
    test = FrobeniusDistance(lastmatrix,newmatrix)
    Flist.append(test)
    ulist.append(u)
    lastmatrix = newmatrix
    us[0] = us[1]
    tests[0] = tests[1]
    us[1] = u
    tests[1] = test
    plt.ion()
    plt.plot(us, tests)  
    plt.pause(0.001)
    u += 1    
    i += 1
    if i == seqsum:
        i = 0
    continue_0_num = continue_num(Flist)
    if continue_0_num > seqsum:
        break
print(df2)
with open(r"C:\Users\admin\Desktop\rotation\Python_assignment\9-gibbs.csv",'w',newline='') as f1:
    df2.to_csv(f1,index=False)
print(newmatrix)
with open(r"C:\Users\admin\Desktop\rotation\Python_assignment\9-gibbsmatrix.csv",'w',newline='') as f2:
    newmatrixdf = pd.DataFrame(newmatrix,index = ['A','C','G','T'])
    newmatrixdf.to_csv(f2)
plt.ioff()
plt.show()
plt.plot(Flist)
plt.show()
