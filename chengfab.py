# -*- coding: utf-8 -*-
# @Author: jingl12
# @Date:   2018-11-17 14:45:59

'''
Python实现，九九乘法表
Python implementation,multiplication table
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end=' ')
    print()
