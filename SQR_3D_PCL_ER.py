# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:20:30 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:20:57 2019

@author: cyc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:41:43 2019

@author: cyc
"""

import random

class sqr_3D_pcl(object):
    rt = []#每个网格的根节点
    sz = []#树的大小
    l = 0#网格边长
    
    def __init__(self,n):
        self.rt.clear()
        self.sz.clear()
        self.l = n
        i = 0
        while (i < n*n*n):#生成n*n*n的一维数组表示网格
            self.rt.append(i)#初始状态每个节点的根节点都是其自身
            self.sz.append(1)#初始状态每个树的大小都是它自身
            i += 1
    
    def find(self,x):#找到x结点的根节点
        while(x != self.rt[x]):
            x = self.rt[x]
        return x
    
    def chk_connected(self,x,y):#检查x，y的根节点，若根节点相同则为已连接
        if (self.find(x) == self.find(y)):
            return True
        else:
            return False
    
    def union(self,x,y):
        rt_x = self.find(x)
        rt_y = self.find(y)
        if (not self.chk_connected(x,y)):
            if (self.sz[rt_x] < self.sz[rt_y]):#比较树的大小，将小树连到大树上
                self.rt[rt_x] = rt_y
                self.sz[rt_y] += self.sz[rt_x]
            else:
                self.rt[rt_y] = rt_x
                self.sz[rt_x] += self.sz[rt_y]
    
    def random_pick(self,k):
        #上面的角
        if (k == 0):#左上后角格点
            di = random.randint(0,2)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择下边的节点
                return k+self.l*self.l
        elif (k == self.l-1):#右上后角格点
            di = random.randint(0,2)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择下边的节点
                return k+self.l*self.l
        elif (k == self.l*(self.l-1)):#左上前角格点
            di = random.randint(0,2)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择下边的节点
                return k+self.l*self.l
        elif (k == self.l*self.l-1):#右下角格点
            di = random.randint(0,2)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择下边的节点
                return k+self.l*self.l
        #下面的角
        if (k == self.l*self.l*self.l-self.l*self.l):#左下后角格点
            di = random.randint(0,2)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
        elif (k == self.l*self.l*self.l-self.l*self.l+self.l-1):#右下后角格点
            di = random.randint(0,2)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
        elif (k == self.l*self.l*self.l-self.l):#左下前角格点
            di = random.randint(0,2)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
        elif (k == self.l*self.l*self.l-1):#右下前角格点
            di = random.randint(0,2)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
        
        
        
        #边
        #上面的边                                
        elif (k > 0 and k < self.l-1):#上后边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
        elif (k > self.l*(self.l-1) and k < self.l*self.l-1):#上前边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
        elif (k % self.l == 0 and k < self.l*(self.l-1) and k > 0):#上左边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
        elif ((k+1) % self.l == 0 and k < self.l*self.l-1 and k > self.l-1):#上右边缘
            di = random.randint(0,3)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
        #下面的边
        elif (k < self.l*self.l*self.l-self.l*self.l+self.l-1 and k > self.l*self.l*self.l-self.l*self.l):#下后边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif (k > self.l*self.l*self.l-self.l and k < self.l*self.l*self.l-1):#下前边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择后边的节点
                return k-self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif (k % self.l == 0 and k < self.l*self.l*self.l-self.l and k > self.l*self.l*self.l-self.l*self.l):#下左边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif ((k+1) % self.l == 0 and k < self.l*self.l*self.l-1 and k > self.l*self.l*self.l-self.l*self.l+self.l-1):#下右边缘
            di = random.randint(0,3)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        #中间的边
        elif (k % (self.l*self.l) == 0 and k > 0 and k < self.l*self.l*self.l-self.l*self.l):#左后边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择下边的节点
                return k+self.l*self.l
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif ((k-self.l+1) % (self.l*self.l) == 0 and k > self.l-1 and k < self.l*self.l*self.l-self.l*self.l+self.l-1):#右后边缘
            di = random.randint(0,3)
            if (di == 0):#选择下边的节点
                return k+self.l*self.l
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif ((k-self.l*self.l+self.l) % (self.l*self.l) == 0 and k < self.l*self.l*self.l-self.l and k > self.l*self.l-self.l):#左前边缘
            di = random.randint(0,3)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择下边的节点
                return k+self.l*self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
        elif ((k-self.l*self.l+1) % (self.l*self.l) == 0 and k > self.l*self.l-1 and k < self.l*self.l*self.l-1):#前右边缘
            di = random.randint(0,3)
            if (di == 0):#选择左边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择后边的节点
                return k-self.l
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
            
        
        
        
        #面
        #上下的面
        elif (k > self.l-1 and k < self.l*self.l-self.l and k % self.l != 0 and (k+1) % self.l != 0):#上
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
            if (di == 4):#选择后边的节点
                return k-self.l
        elif (k > self.l*self.l*self.l-self.l*self.l+self.l-1 and k < self.l*self.l*self.l-self.l and k % self.l != 0 and (k+1) % self.l != 0):#下
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择上边的节点
                return k-self.l*self.l
            if (di == 4):#选择后边的节点              
                return k-self.l
        #左右的面
        elif (k % self.l == 0 and k > 0 and k < self.l*self.l*self.l-self.l and k % (self.l*self.l) != 0 and (k-self.l*self.l+self.l) % (self.l*self.l) != 0):#左
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
            if (di == 4):#选择后边的节点
                return k-self.l
        elif ((k+1) % self.l == 0 and k > self.l-1 and k < self.l*self.l*self.l-1 and (k-self.l+1) % (self.l*self.l) != 0 and (k-self.l*self.l+1) % (self.l*self.l) != 0):#右
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k-1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
            if (di == 4):#选择后边的节点
                return k-self.l
        #前后两面
        elif (k % (self.l*self.l) > 0 and k % (self.l*self.l) < self.l-1 and k > self.l-1 and k < self.l*self.l*self.l-self.l*self.l):#后
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
            if (di == 4):#选择左边的节点
                return k-1
        elif (k % (self.l*self.l) > self.l*self.l-self.l and k % (self.l*self.l) < self.l*self.l-1 and k > self.l*self.l-1 and k < self.l*self.l*self.l-self.l):#前
            di = random.randint(0,4)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择左边的节点
                return k-1
            if (di == 2):#选择上边的节点
                return k-self.l*self.l
            if (di == 3):#选择下边的节点
                return k+self.l*self.l
            if (di == 4):#选择后边的节点
                return k-self.l
        #中间格点
        else:
            di = random.randint(0,5)
            if (di == 0):#选择右边的节点
                return k+1
            if (di == 1):#选择前边的节点
                return k+self.l
            if (di == 2):#选择左边的节点
                return k-1
            if (di == 3):#选择后边的节点
                return k-self.l
            if (di == 4):#选择下边的节点
                return k+self.l*self.l
            if (di == 5):#选择上边的节点
                return k-self.l*self.l
      
    def grid_union(self):
        i1 = 0
        j1 = 0
        while (self.chk_connected(i1,j1)):
            i1 = random.randint(0,self.l*self.l*self.l-1)
            j1 = self.random_pick(i1)
        self.union(i1,j1)
        