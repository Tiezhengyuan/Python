# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:33:46 2015

@author: yuan
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs



#the standard normal distribution
u1=0;var1=1
a1=np.random.normal(u1,var1, 1000)#mean=0, var=1
n1, bins1, patches1=plt.hist(a1, 50, normed=1, 
   facecolor='white', edgecolor='black', alpha=.5)
plt.text(-3, .4, 'mean={}\nvariance={}'.format(u1, var1))
y1 = scs.norm.pdf(bins1, u1, var1)#fitted line
plt.plot(bins1, y1, '-', color='red',linewidth=3)
plt.axvline(x=u1,color='black', linewidth=1)
plt.title("Gausian Distribution")
plt.xlabel('random values')
plt.ylabel('frequency')
 
#normal distribution
#
u2=6#mean
var2=4#variance
a2=np.random.normal(u2,var2, 1000)
#1
n1,bins1,patches1=plt.hist(a1, 50, normed=1, facecolor='red',alpha=.5)
y1 = scs.norm.pdf(bins1, u1, var1)#fitted line
plt.plot(bins1, y1, '-', color='blue',linewidth=3)
plt.axvline(x=u1,color='black', linewidth=1)
plt.text(u1+1,.4, 'mean={}\nvariance={}'.format(u1,var1))
#2
n2,bins2,patches2=plt.hist(a2, 50, normed=1, facecolor='blue',alpha=.5)
y2 = scs.norm.pdf(bins2, u2, var2)#fitted line
plt.plot(bins2, y2, '-', color='blue',linewidth=3)
plt.axvline(x=u2,color='black', linewidth=1)
plt.text(u2+1,.15, 'mean={}\nvariance={}'.format(u2,var2))
#other options
plt.xlim(xmin=-10,xmax=20)
plt.ylim(ymin=0,ymax=.5)
plt.title('Comparison of Two Normal Distributions')
plt.xlabel('Values')
plt.ylabel('Density')
plt.show()

#https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html
#histogram
df=pd.read_csv('gapminder-FiveYearData.csv',header=0, index_col=None)
df
#expected life
df1 = df.loc[(df.year<=1981)]
df2 = df.loc[(df.year>=1982)]
plt.cla
plt.hist(df1.lifeExp, bins=30, color="blue", alpha=.5)
plt.hist(df2.lifeExp, bins=30, color="green", alpha=.5)
plt.text(40, 50, '1952-1981')
plt.text(60, 80, '1922-2007')
plt.title("Frequency of expected life")
plt.xlabel("year")
plt.ylabel("frequency")

