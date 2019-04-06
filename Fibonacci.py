# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 23:50:36 2018

@author: Dolam
"""
import time
start_time = time.time()
num = 2
a = 1
b = 1
#print a
#print b
while (time.time() - start_time) <= 15.000000000:
    c = a + b
    a = b
    b = c 
    num += 1
#    print c
print str(num) + ' Fibonacci numbers were computed in %s seconds' % (time.time() - start_time)

    