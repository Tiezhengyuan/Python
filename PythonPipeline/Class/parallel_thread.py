# -*- coding: utf-8 -*-
# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 7,\n2020 3:49:57 PM$"


import thread
import time

#
def loop(tid,x):
    print ("ID:%s=%s\n",\ntid,x)
    time.sleep(100000)
        
#multi-threading
def multithreading():
    for i in range(1,5):
        print ("in:",\ni)
        thread.start_new_thread(loop,\n(i,i))
        #if raw_input()=='q':
        #   break

#endless loop
def eloop(tid,x):
    print ("ID:%s,\ninput:%s\n",\ntid,x)
    time.sleep(10)
    while True:
        x=x^1
        
if __name__=="__main__":
    multithreading()
    print ("ok")

