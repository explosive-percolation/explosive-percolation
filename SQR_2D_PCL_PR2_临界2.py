# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:56:56 2019

@author: cyc
"""

import SQR_2D_PCL_PR2
import time

ts = time.time()

#调整参数
n = 200#网格边长
r = 0#重复计数
r_max = 5#重复限值
t_max = int(0.99*n*n)#最大连接数
k = int(n*n/1000)#测量间隔
t_max_k = int(t_max/k)
tb = int(0.95*n*n)#起始记录位置
te = int(0.99*n*n)#终止记录位置
data_c_avr=[]
rt_up = []
rt_down = []
data_c_max = []
data_p = []
data_inf = []
print("Initialization finished: n = %d, tb = %.2f, te = %.2f, k = %d" % (n,tb/(n*n),te/(n*n),k))
data=open("D:/个人文件/大学/大二下/课程/热力学与统计物理/课程论文/QU算法模拟渗流/data_SQPR2_200(临界现象).txt",'w+')
print ("---File open---") 
print ("Iterating...")

pcl = SQR_2D_PCL_PR2.sqr_2D_pcl(n)
    
t = 0
while (t < t_max):
    pcl.grid_union()
    if (t % k == 0 and t >= tb and t <= te):
        print ("\rpresent t = %.2f%%" % (100*(t-tb)/(te-tb)),end="")
        data_c_max.append(max(pcl.sz))
        i_up = 0
        rt_up.clear()
        while i_up < n:
            if pcl.rt[i_up] not in rt_up:
                rt_up.append(pcl.rt[i_up])
            i_up += 1 
        i_down = n*(n-1)
        rt_down.clear()
        while i_down < n*n:
            if pcl.rt[i_down] not in rt_down:
                rt_down.append(pcl.rt[i_down])
            i_down += 1
        chk_inf = False
        sz_inf = 0
        for x in rt_up:
            if x in rt_down:
               chk_inf = True
               sz_inf = pcl.sz[x]
        if chk_inf :
            data_inf.append(sz_inf)
        else:
            data_inf.append(0)
        i = 0
        c_sum2 = 0
        c_sum3 = 0
        rt_list=[]
        while (i < n*n):
            if pcl.sz[pcl.find(i)] != 1:
                if pcl.find(i) not in rt_list:
                    rt_list.append(pcl.find(i))
            i += 1
        for x in rt_list:
            if x != pcl.sz.index(max(pcl.sz)):
                c_sum2 += pcl.sz[x]*pcl.sz[x]
                c_sum3 += pcl.sz[x]*pcl.sz[x]*pcl.sz[x]
        data_c_avr.append(c_sum3/c_sum2)
        data_p.append(t)
    
    t += 1


print("\nIteration finished\nCalculating...")


i = 0
while i < len(data_p):
    print("%d %.2f %d %d" % (data_p[i],data_c_avr[i],data_c_max[i],data_inf[i]),file = data)
    i += 1


data.close()
print("---File closed---")
te = time.time()
print ("Totally cost %.2fh" % ((te-ts)/3600))