# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:25:46 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:58:46 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:56:56 2019

@author: cyc
"""

import SQR_3D_PCL_ER
import numpy as np
import time
from mpl_toolkits.mplot3d import Axes3D

ts = time.time()

#调整参数
n = 50#网格边长
r = 0#重复计数
r_max = 1#重复限值
t_max = 0.995*n*n*n#最大连接数
k = n*n*n/1000#测量间隔
max_site = []
t_max_k = int(t_max/k)
data_array = np.zeros((r_max,t_max_k))
print("Initialization finished: n = %d, r_max = %d, k = %d" % (n,r_max,k))
print ("Iterating...")

while (r < r_max):#对同一t循环取平均
    print("Present r = %d" % (r+1))
    pcl = SQR_3D_PCL_ER.sqr_3D_pcl(n)
    t = 0
    while (t < t_max):
        pcl.grid_union()
        max_site.clear()
        if (t % k == 0):
            print ("\rpresent t = %.2f%%" % (100*t/t_max),end="")
        if t == 0.72*n*n*n :
            max_sz = pcl.sz.index(max(pcl.sz))
            max_rt = pcl.rt[max_sz]
            i = 0
            while (i < n*n*n):
                if pcl.find(i) == max_rt:
                    max_site.append(1)
                else:
                    max_site.append(0)
                i += 1
            plot_x = []
            plot_y = []
            plot_z = []
            i = 0
            while i < n*n*n:
                if max_site[i] == 1:
                    plot_x.append(i%n)
                    plot_y.append(int(i%(n*n)/n))
                    plot_z.append(int(i/(n*n)))
                i += 1
            import matplotlib.pyplot as plt
            im = plt.subplot(111,projection = '3d')
            im.scatter(plot_x,plot_y,plot_z,c='b',marker='s')
            plt.show()#输出所有为1的格点（用蓝色标注）
        if t == 0.73*n*n*n :
            max_sz = pcl.sz.index(max(pcl.sz))
            max_rt = pcl.rt[max_sz]
            i = 0
            while (i < n*n*n):
                if pcl.find(i) == max_rt:
                    max_site.append(1)
                else:
                    max_site.append(0)
                i += 1
            plot_x = []
            plot_y = []
            plot_z = []
            i = 0
            while i < n*n*n:
                if max_site[i] == 1:
                    plot_x.append(i%n)
                    plot_y.append(int(i%(n*n)/n))
                    plot_z.append(int(i/(n*n)))
                i += 1
            
            import matplotlib.pyplot as plt
            im = plt.subplot(111,projection = '3d')
            im.scatter(plot_x,plot_y,plot_z,c='b',marker='s')
            plt.show()#输出所有为1的格点（用蓝色标注）
            
        
        t += 1
    r += 1
    print("")

te = time.time()
print ("Totally cost %.2fh" % ((te-ts)/3600))