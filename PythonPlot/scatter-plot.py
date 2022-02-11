# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 09:49:42 2015

@author: yuan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

#function of scatter plot
def scatterplot(x, y, xlab='x', ylab='y', xlim=(), ylim=(), col='black', 
                lty='-', main='plot'):
    
    if len(xlim)==0:
        xlim=(min(x),max(x))
    if len(ylim)==0:
        ylim=(min(y),max(y))

    #plot
    plt.plot(x,y, color=col, linestyle=lty)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.suptitle(main, fontsize=20)
    plt.show()

#default
x=np.arange(10)
y=np.arange(10,20)
plt.plot(x,y)    

#more options
plt.cla()#clear plot
plt.plot(x, y, color='grey', linestyle='solid', linewidth=1.5, 
         marker='o', markersize=10, markerfacecolor='red', 
         markeredgecolor='blue')
plt.xlim(-1,10)
plt.ylim(9,20)
plt.xlabel('Number',fontsize=10)
plt.ylabel('Values', fontsize=10)
plt.title('scatter plot', fontsize=30)
plt.show()#show plot

#plot3           
r1=np.random.randn(100).cumsum()
r2=np.random.randn(100).cumsum()
#draw line plot
plt.plot(r1, linestyle='--', color='black', linewidth=2)
plt.plot(r2, linestyle='-', color='red')
plt.title('Time Profile', fontsize=30)
plt.xlabel('time, min')
plt.ylabel('value factor')
plt.legend(['r1','r2'], loc=4)

#plot4
#y~x
x=np.arange(10)
y=np.array(5*x+10)+np.random.rand(10)*10
# Fit with polyfit
slope, intercept = np.polyfit(x, y, deg=1)#one degree
#draw plot
plt.cla()#clear plot
plt.scatter(x,y, color='red',edgecolor='black',marker='^', s=30)
plt.plot(x, intercept+slope*x, '-')#draw fitted line
plt.title("x vs. y")
plt.xlabel('x')
plt.ylabel('y')
#add arrows
plt.annotate('The fitted line',ha='center',va='bottom', 
             xy=(5,40), xytext=(2,50), 
             arrowprops={'facecolor':'blue','shrink':.05})
#add annotation
box={'facecolor':'tan', 'edgecolor':'tan', 'boxstyle':'round'}
formula_text='Y={}X+{}'.format(round(slope,4),round(intercept,4))
plt.text(0,60, formula_text, bbox=box)
#plt.show()#show plot


#dots style options
markers = ['.', 'o', '^', 'v', '<', '>', '+', '*', 's', 'd']
colors= ['black','red','blue', 'green','grey', 'purple', 
         'yellow','brown','tan', 'pink','torpoise']
for i in np.arange(len(markers)):
    plt.scatter(i,i*2, s=i*25+100, marker=markers[i], c=colors[i])
    style = "s={},marker=\'{}\',c=\'{}\'".format(i*100+100, markers[i], colors[i])
    plt.text(i+.5, i*2-.1, style)
plt.xlim(-1,20)
plt.show()

#line style options
colors= ['black','red','blue', 'green','grey', 'purple', 
         'yellow','brown','tan', 'pink']
styles=['-','--',':','-.']
for i in range(len(styles)):
    plt.plot(np.arange(len(styles)), [i]*len(styles), 
       color=colors[i], linestyle=styles[i], linewidth=4)
    plt.text(0, i-.3, "color=\'{}\',linestyle=\'{}\'".format(colors[i],styles[i]) )
plt.ylim(-1, 4)
plt.show()


#volcano plot
DEG=pd.read_csv('differential_expressed_genes.csv', 
                header=0, index_col=0)
DEG.shape
list(DEG)
DEG
#
cond1= DEG['PValue']<=0.05
cond2 = DEG['logFC']>=1
cond3 = DEG['logFC']<=-1
up=DEG.loc[ cond1 & cond2 ]
plt.scatter(up.logFC, -np.log10(up.PValue), marker='^', c='red')
down=DEG.loc[cond1 & cond3]
plt.scatter(down.logFC, -np.log10(down.PValue), marker='v', c='blue')
normal=DEG.loc[ ~( (cond1 & cond2)|(cond1 & cond3) )]
plt.scatter(normal.logFC, -np.log10(normal.PValue), marker='.', c='black')
plt.axvline(x=0, color='black')
plt.xlabel("log2 of Fold change")
plt.ylabel("-log10 of p value")
plt.title('DEG analysis', fontsize=30)

