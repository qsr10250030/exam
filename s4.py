#!/usr/bin/env python
# -*- coding:utf-8 -*-


# d={"3":4}
# # if d.get("2",None):
# #     print(1)
# # else:
# #     print(2)
# d={'name1':'a','name2':'b','name3':'c','name4':'d'}
# print("  ".join(d.values()))
# print(sorted(d.values()))
# d={}
# for item in range(10):
#     dis= item-5 if item -5>=0 else 5-item
#     d[dis]=item
# print(d)
# print(d.get(0))
a = [i for i in range(5)]
f =lambda x:x**2
b = map(f,a)
print(b)
kk = lambda x,y :x+y

c = map(kk,a,b)
print(c)