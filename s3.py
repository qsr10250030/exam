#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


if __name__=="__main__":
    h,n = str(sys.stdin.readline().strip()).split()
    hh = str(sys.stdin.readline().strip()).split()
    d={}
    li=[]
    sorted_li=[]
    h = int(h)
    n = int(n)
    if len(hh)==n:
        for item in hh:
           dis = int(item) -h
           d[dis]=item
           if dis<0:
               li.append(dis*-1)
           else:
               li.append(dis)
        li = set(li)
        li = list(li)
        li = sorted(li)
        for item in li:
            if item :
                if d.get(-1*item,None):
                    sorted_li.append(d.get(item*-1))
                if d.get(item,None):
                    sorted_li.append(d.get(item))
            else:
                if d.get(item,None):
                    sorted_li.append(d.get(item))
        s = " ".join(sorted_li)
        print(s)



