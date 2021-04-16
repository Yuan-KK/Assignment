import os
import pandas as pd
import numpy as np
import re
# 读取文件*（读取文件名list，for每一个文件.report )
alphabet = {'U':'0','R':'1','D':'2','K':'3','P':'4','C':'5','O':'6','F':'7','G':'8','S':'9'}
alpharev = {'0':'U','1':'R','2':'D','3':'K','4':'P','C':'5','6':'O','7':'F','8':'G','9':'S'}
fList = os.listdir(r'C:\Users\admin\Desktop\rotation')
for i in range(len(fList)):
    newfile = fList[i].split('.')[0] + '.csv'
    if '.report' in fList[i]:
        df = pd.read_table(r"C:\Users\admin\Desktop\rotation\\" + fList[i], header = None)
        # 提取rank列，并去重复
        rank = df[3].tolist()
        rank = list(set(rank))
        rank_new = []    
        for i in rank :
            v = re.sub("\D", "",i) 
            u = re.findall(r'[A-Za-z]', i)
            u = str(u[0])
            for key,value in alphabet.items():
                u = u.replace(key,value)
            l = (u,v)
            rank_new.append(l)
            rank_new.sort(key=lambda x:(x[0],x[1]))
            rankn= [] 
            for a in rank_new:
                tup1 = a[0]
                tup2 = a[1]
                for key,value in alpharev.items():
                    tup1 = tup1.replace(key,value)
                tup = (tup1,tup2)
                rankn.append(tup)
        rank = []
        for m in rankn:
            m = m[0]+str(m[1])
            rank.append(m)
        # 按照rank的元素依次在文件中筛选行
        with open (r"C:\Users\admin\Desktop\rotation\output\\" + newfile,'w+',newline='') as nf:
            for j in rank:
                df_new = df[(df[3] == j)][[0,1,3,5]]
                df_new = df_new.reset_index(drop=True)
                taxname = df_new[5].tolist()
                newtaxname = []
                for name in taxname:
                    newname = name.lstrip()
                    newtaxname.append(newname)
                df_new[5] = newtaxname
                allreads = df[2].sum()
                reads = df_new[1].tolist()
                per_count = []
                for k in reads:
                    k /= allreads 
                    k *= 100
                    per_count.append(k)
                df_new['%_count'] = per_count
                
                # 添加一行
                uncreads = allreads - df_new[1].sum()
                unper = 100 - df_new[0].sum()
                unpercount = 100 - df_new['%_count'].sum()
                unc = pd.DataFrame({0: unper,
                  1: uncreads,
                  3:'U',
                  5: 'unclassified',
                  '%_count': unpercount},
                  index=[1])
                newrank = df_new[3].tolist()
                if 'U' not in newrank:
                    df_new = df_new.append(unc,ignore_index=True)
                df_new.columns=['%','reads','rank','taxName','%_count']
                df_new = df_new.sort_values(by='%_count',ascending=False)
                df_new.to_csv (nf,index=False)
