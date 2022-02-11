#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:34:27 2020

@author: yuan
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


#draw pieplot
d=[30,30,4.2,20,9,6.8]
col=['lightgrey','lightgreen']*3
names=list('ABCDEF')
#
plt.cla()
plt.pie(d,colors=col,labels=names, autopct='%1.1f%%',
        pctdistance=.85, labeldistance=1.1)
plt.axis('equal')
plt.title('Income pecentage of departments')
plt.show()
 

#data
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
explode = (0, 0, 0, 0.25)  # only "explode" the 2nd slice
logs_labels = ['A', 'B', 'C']
logs_sizes = [15, 30, 55]
#plot
fig = plt.figure()
#pie1
ax1 = fig.add_axes([.1, .1, .8, .8], aspect=1)
ax1.pie(sizes, explode=explode, labels=labels, 
        autopct='%1.1f%%', shadow=True, startangle=50)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal') 
#pie2
ax2 = fig.add_axes([.65, .65, .5, .5], aspect=1)
ax2.pie(logs_sizes, labels=logs_labels, autopct='%1.1f%%', radius=.8)
plt.title('Income pecentage of departments')
plt.show()

