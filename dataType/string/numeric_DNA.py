# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:46:39 2017

@author: yuan
"""

p=list('ATGC')
pool={}

i=0
for a in p:
    pool[a]=i
    i+=1
    for b in p:
        pool[a+b]=i
        i+=1
        for c in p:
            pool[a+b+c]=i
            i+=1
            for d in p:
                pool[a+b+c+d]=i
                i+=1
print i, pool