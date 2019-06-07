# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:41:38 2019

@author: cyc
"""

class ER(object):
    rt = []#每个网格的根节点
    sz = []#树的大小
    l = 0#网格边长
    
    def __init__(self,n):
        self.rt.clear()
        self.sz.clear()
        self.N = n
        i = 0
        while (i < self.N):#生成长度为n的一位数组表示网格
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
    
    