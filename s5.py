#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
init_data =[['time1','a',0, 1, 2],
       ['time1','b',3, 4, 5],
       ['time1','c',8, 7, 6],
            ['time2','a', 1, 1, 2],
            ['time2','b', 3, 4, 5],
            ['time2','c', 4, 7, 6],
            ]
data = pd.DataFrame(init_data,columns=["time","name","cpu","mem",'io'])
data=data[["name","cpu","time"]]
ret =data.pivot(index="name",columns="time",values="cpu")
# ret.reset_index(inplace=True)
print(ret)

# data = np.array(init_data)
# print(data.T)
# print(data)
# print ("matrix 取 1行")
# print(data[0])
# print("matrix 取1列")
# print(data[:,[0,3]])
# print("获取每行的平均数")
# ret =data.mean(axis=1)
#
# print(ret,ret.shape)
# print(ret.reshape(3,1))
# print(ret)
# test=np.c_[data,ret]
# print(test)
# print("获取每列的平均数")
# ret=data.mean(axis=0)
# print(ret.shape)
# print(data.shape)
# # test= np.insert(data,3,values=ret,axis=0)
# test = np.r_[data,ret.reshape(1,3)]
# print(test)
#
# test1 = data[:,-1]
# print("test1={}".format(test1))
# test2 =data[:,0]
# print("test2={}".format(test2))
# ret=test1-test2
# ret = map(lambda x: 1 if x>0 else 0 ,ret)
# print(ret)