#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:36:49 2020

@author: yuan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#boxplot
a1=np.random.rand(100,5)#matrix with 100 rows, 5 columns
a1.shape
plt.cla()
plt.boxplot(a1, 1, 'gD')
plt.axhline(y=.5,color='black', linestyle='dashed', linewidth=1)
plt.ylim(ymin=-.1,ymax=1.2)
plt.title('Boxplot')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.show()

#boxplot in pandas
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
df=pd.read_csv('gapminder-FiveYearData.csv',header=0, index_col=None)
df['logPop']=np.log(df['pop'])
#draw boxplot
boxprops = dict(linestyle='-', linewidth=2, color='blue')
medianprops = dict(linestyle='-', linewidth=4, color='green')
df.boxplot(column='logPop', by="continent", rot=45, 
           grid=False, notch=True, boxprops=boxprops,
           medianprops=medianprops, return_type='dict')
plt.title("Population grouped by continent") #new title
plt.suptitle('')#remove sub-stitle
plt.xlabel("Continents")
plt.ylabel("log of population")


#multiple
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(18,6))
df.boxplot(column='logPop', by="continent", ax=ax1,
    rot=45, grid=False, notch=True, boxprops=boxprops,
    layout=(1,3),medianprops=medianprops, return_type='dict')
ax1.set_title('Population')
ax1.set_ylabel('Log million')
df.boxplot(column= 'lifeExp', by="continent", ax=ax2,
    rot=45, grid=False, notch=True, boxprops=boxprops,
    layout=(1,3),medianprops=medianprops, return_type='dict')
ax2.set_title('expected life span')
ax2.set_ylabel('Year')
df.boxplot(column= 'gdpPercap', by="continent", ax=ax3,
    rot=45, grid=False, notch=True, boxprops=boxprops,
    layout=(1,3),medianprops=medianprops, return_type='dict')
ax3.set_title("GDP")
ax3.set_ylabel("million USD")
fig.suptitle("Population grouped by continent", fontsize=20) 
fig.subplots_adjust(left=.4, right=1.2, hspace=.2)

