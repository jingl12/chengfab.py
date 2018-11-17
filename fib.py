# -*- coding: utf-8 -*-
# @Author: 境
# @Date:   2018-11-17 16:56:26

'''
Python实现斐波那契数列
Python implements the Fibonacci sequence
'''
#100内的斐波那契数列（Fibonacci Numbers in 100）

lst = [0,1]
for i in range(2,20):
    lst.append(lst[i-1] + lst[i-2])
    if lst[i]>100:
        lst.pop(i)
        break

print(lst)
print('-'*20)


