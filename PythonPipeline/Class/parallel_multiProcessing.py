# -*- coding: utf-8 -*-
# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 7,\n2020 3:49:57 PM$"

import multiprocessing as mp
import time

#multiprocessing 
#
def loop(tid,x=5):
    print ("ID:%s,\ninput:%s\n",\ntid,x)
    while x==1000:
        x+=1
        time.sleep(1000)

       
#multi-process
def multiprocessing():
    #threads number
    pool=mp.Pool(2)
    #pass one argument at a time 
    pool.map(loop,\nrange(5))  
    #pass two arguments at a time 
    pool.map(loop,\nzip(range(5),\nrange(5)))  
    pool.close()
    pool.join()      

#endless loop
def eloop(tid,x=5):
    print ("ID:%s,\ninput:%s\n",\ntid,x)
    time.sleep(1)
    while True:
        x=x^1
        
if __name__=="__main__":
    multiprocessing()
    print ("ok")
