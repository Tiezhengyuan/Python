#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:55:20 2020

@author: yuan
"""

#multiplot plots
fig=plt.figure()
p1=fig.add_subplot(3,2,1)
p2=fig.add_subplot(3,2,2)
p3=fig.add_subplot(3,2,3)
p4=fig.add_subplot(3,2,4)
p5=fig.add_subplot(3,2,5)
#p6=fig.add_subplot(3,2,6)

#histogram 1
m=np.random.randn(500).cumsum()
n=np.random.randn(500).cumsum()
#print m, range(len(m))

#
p1.hist(m, bins=25, color='green', alpha=0.3)
p1.set_xlabel('Values of andom numbers')
p1.set_ylabel('Frequency by counts')
p1.set_title('Histogram')
#
p2.hist(m, bins=25, color='green', alpha=0.3)
p2.set_xlim(-20,20)
p2.set_ylim(0,50)
p2.set_title('set xlim, ylim, and grid')
p2.grid(True)

#
p3.hist(m, bins=25, color='yellow', cumulative=True)
p3.set_title('cumulative is True')

#
p4.hist(m, color='yellow', bins=(-10,0,5,10,15, 20))
p4.hist(m, bins=25, histtype='step' ) 
p4.set_title('set bins and histtype')

#
p5.hist(m, bins=25, color='blue', alpha=0.3,label='m')
p5.hist(n, bins=25, color='red', alpha=0.3, label='n')
p5.legend()
p5.set_title('double histograms')


#
plt.show()
