# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:07:42 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:49:00 2019

@author: cyc
"""

import ER_Bond
import random
import time
import numpy as np

ts = time.time()

n_max = 1e5#最大节点数
t_max = int(1.5*n_max)#最大渗流连接数
r = 0
r_max = 5#最大迭代次数
k = n_max/5000#测量间隔
data_array = np.zeros((r_max,int(t_max/k)))
print("Initialization finished: n = %d, r_max = %d" % (n_max,r_max))
data=open("D:/个人文件/大学/大二下/课程/热力学与统计物理/课程论文/QU算法模拟渗流/ER/data_ERER2_1e5.txt",'w+')
print ("---File open---") 
    
print("Iterating...")
while (r < r_max):
    print ("present r = %d" % (r+1))
    PR = ER_Bond.ER(n_max)#生成渗流
    t = 0
    while (t < t_max):
        
        i1 = random.randint(0,PR.N-1)
        j1 = random.randint(0,PR.N-1)
        
        PR.union(i1,j1)
        
    
        #统计最大团簇的大小
       
        if (t % k == 0):
             max_sz = max(PR.sz)
             
             t_k = int(t/k)
             data_array[r][t_k] = max_sz
            
             print ("\rpresent t = %.2f%%" % (100*t/t_max),end="")
        t += 1
    r += 1
    print("")
    
print("\rIteration finished\nCalculating...")
data_mean = []
s1 = 0
while s1 < int(t_max/k):#对测量值取平均
    s2 = 0
    sum0 = 0
    while s2 < r_max:
        sum0 += data_array[s2][s1]
        s2 += 1
    data_mean.append(sum0/r_max)
    s1 += 1

s3 = 0
while s3 < int(t_max/k):
    print("%d %.2f" % ((s3+1)*k,data_mean[s3]),file = data)
    s3 += 1

data.close()
te = time.time()
print("Total cost:%.2fh" % ((te-ts)/3600))