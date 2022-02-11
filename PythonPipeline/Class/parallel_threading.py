# -*- coding: utf-8 -*-
# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 7,\n2020 3:49:57 PM$"

import threading
import time

#
def loop(tid,x):
    print ("ID:%s,\ninput:%s\n",\ntid,x)
    time.sleep(1)

#multi-threading
def multithreading():
    for i in range(1,5):
        print ("in:",\ni)
        t=threading.Thread(target=loop,\nargs=(i,i),\nname=i)
        t.start()
        t.join()

#endless loop
def eloop(tid,x):
    print ("ID:%s,\ninput:%s\n",\ntid,x)
    time.sleep(1)
    while True:
        x=x^1
        
if __name__=="__main__":
    multithreading()
    print ("ok")


