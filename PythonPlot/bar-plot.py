#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:07:09 2020

@author: yuan
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

#draw barplot using plt
a=[30,20,58,10]
b=[35,30,28,40]
index=np.array(range(len(a)))
bar_width=.35
#plot
plt.cla()
plt.bar(index, a, bar_width, color='blue', label='2017')
plt.bar(index+bar_width, b, bar_width, color='red', label='2018')
plt.xticks(index+bar_width, ['A','B','C','D'])
plt.xlabel('group')
plt.ylabel('Productivity, ton')
plt.title('Treatment')
plt.legend()
plt.tight_layout()
plt.show()

#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html
#bar plot using pandas
pro=pd.DataFrame({'2017':a, '2018':b}, index=list('ABCD'))
fig, (ax1,ax2)=plt.subplots(1,2, figsize=(13,6))
#bar1
pro.plot.bar(ax=ax1, rot=0)
ax1.axhline(30)
ax1.set_xlabel("group")
ax1.set_ylabel("productivity tons")
ax1.set_title("vertical pattern")
#bar2
pro.plot.barh(color=['grey','lightgrey'], ax=ax2)
ax2.axvline(30, linestyle="--", color='grey')
ax2.set_ylabel("group")
ax2.set_xlabel("productivity tons")
ax2.legend(loc="lower right")
ax2.set_title("horizontal pattern")
fig.suptitle("productivity of 2017-2018", fontsize=20)
plt.show()


#barplot
df=pd.read_csv('gapminder-FiveYearData.csv',header=0, index_col=None)
df
#organize data
df1=df.groupby('continent').agg({'lifeExp': [np.mean, np.std]})
df1.columns=df1.columns.map('_'.join)
#draw barplot
ax = df1.plot.bar(df1.index, 'lifeExp_mean', color='grey', rot=45, 
    legend=False, title="Expected life span on average (1952-2007)")
ax.errorbar(df1.index, df1.lifeExp_mean, yerr=2*df1.lifeExp_std,
            linewidth=2, color='black', alpha=.3, capsize=5)
ax.lines[0].remove()#remove lines between error bars
plt.ylim(20,90)
plt.xlabel('Continents')
plt.ylabel('year')


#
df1= df.loc[df['year']==1952]
df11=df1.groupby('continent').agg({'lifeExp':np.mean})
df2= df.loc[df['year']==2007]
df21=df2.groupby('continent').agg({'lifeExp':np.mean})
bar_width=[.4]*len(df11)
#plot
plt.bar(df21.index, df21.lifeExp, width=bar_width,  color='lightgreen')
plt.bar(df11.index, -df11.lifeExp, width=bar_width, color='grey')
plt.title("Expected life span on average (1952-2007")
plt.axhline(60, color="grey", linestyle='--')
plt.axhline(-60, color="grey", linestyle='--')
plt.axhline(0, color="black")
plt.text(-.4, -80, "1952")
plt.text(-.4, 80, "2007")
plt.ylim(-90,90)

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

plt.ylim(-1.25, +1.25)