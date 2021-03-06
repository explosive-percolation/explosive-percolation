# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:56:56 2019

@author: cyc
"""

import SQR_2D_PCL_PR2
import numpy as np
import time

ts = time.time()

#调整参数
n = 5000#网格边长
r = 0#重复计数
r_max = 5#重复限值
t_max = int(0.995*n*n)#最大连接数
k = int(n*n/1000)#测量间隔
t_max_k = int(t_max/k)
data_array = np.zeros((r_max,t_max_k+1))
print("Initialization finished: n = %d, r_max = %d, k = %d" % (n,r_max,k))
data=open("D:/个人文件/大学/大二下/课程/热力学与统计物理/课程论文/QU算法模拟渗流/data_SQPR2_5000.txt",'w+')
print ("---File open---") 
print ("Iterating...")

while (r < r_max):#对同一t循环取平均
    print("Present r = %d" % (r+1))
    pcl = SQR_2D_PCL_PR2.sqr_2D_pcl(n)
    t = 0
    while (t < t_max):
        pcl.grid_union()
        if (t % k == 0):
            max_sz = pcl.sz.index(max(pcl.sz))
            max_rt = pcl.rt[max_sz]
            i = 0
            gcount = 0
            while (i < n*n):
                if pcl.find(i) == max_rt:
                    gcount += 1
                i += 1
            t_k = int(t/k)
            data_array[r][t_k] = gcount
            print ("\rpresent t = %.2f%%" % (100*t/t_max),end="")
        t += 1
    r += 1
    print("")


print("\rIteration finished\nCalculating...")
data_mean = []
s1 = 0
while s1 < t_max_k:#对测量值取平均
    s2 = 0
    sum0 = 0
    while s2 < r_max:
        sum0 += data_array[s2][s1]
        s2 += 1
    data_mean.append(sum0/r_max)
    s1 += 1

s3 = 0
while s3 < t_max_k:
    print("%d %.2f" % ((s3+1)*k,data_mean[s3]),file = data)
    s3 += 1


data.close()
print("---File closed---")
te = time.time()
print ("Totally cost %.2fh" % ((te-ts)/3600))