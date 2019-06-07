# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:27:57 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:19:57 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:43:05 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:06:31 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:56:56 2019

@author: cyc
"""

import ER_Bond
import random
import time

ts = time.time()

#调整参数
n_max = 1e5#最大节点数
r = 0#重复计数
r_max = 5#重复限值
t_max = int(0.60*n_max)#最大连接数
k = int(n_max/1000)#测量间隔
t_max_k = int(t_max/k)
tb = int(0.45*n_max)#起始记录位置
te = int(0.55*n_max)#终止记录位置
data_c_avr=[]
rt_up = []
rt_down = []
data_c_max = []
data_p = []
print("Initialization finished: n = %d, tb = %.2f, te = %.2f, k = %d" % (n_max,tb/(n_max),te/(n_max),k))
data=open("D:/个人文件/大学/大二下/课程/热力学与统计物理/课程论文/QU算法模拟渗流/data_RNER2_1e4(临界现象).txt",'w+')
print ("---File open---") 
print ("Iterating...")

PR = ER_Bond.ER(n_max)#生成渗流
    
t = 0

while (t < t_max):
    i1 = random.randint(0,PR.N-1)
    i2 = random.randint(0,PR.N-1)
     

    
        
    
    PR.union(i1,i2)
    
    if (t % k == 0 and t >= tb and t <= te):
        print ("\rpresent t = %.2f%%" % (100*(t-tb)/(te-tb)),end="")
        data_c_max.append(max(PR.sz))
        
        i = 0
        c_sum2 = 0
        c_sum3 = 0
        rt_list=[]
        while (i < n_max):
            if PR.sz[PR.find(i)] != 1:
                if PR.find(i) not in rt_list:
                    rt_list.append(PR.find(i))
            i += 1
        for x in rt_list:
            if x != PR.sz.index(max(PR.sz)):
                c_sum2 += PR.sz[x]*PR.sz[x]
                c_sum3 += PR.sz[x]*PR.sz[x]*PR.sz[x]
        data_c_avr.append(c_sum3/c_sum2)
        data_p.append(t)
    
    t += 1


print("\nIteration finished\nCalculating...")


i = 0
while i < len(data_p):
    print("%d %.2f %d" % (data_p[i],data_c_avr[i],data_c_max[i]),file = data)
    i += 1


data.close()
print("---File closed---")
te = time.time()
print ("Totally cost %.2fh" % ((te-ts)/3600))