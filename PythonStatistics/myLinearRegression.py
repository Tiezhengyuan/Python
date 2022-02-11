#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:23:46 2020

@author: yuan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing, model_selection

"""
Y
predY=reg.predict(X)
residual_plot(Y, predY)
"""
def residual_plot(Y, predY):
    res = Y - predY
    RSS = round(np.sum(res**2))
    #
    lm=linear_model.LinearRegression(fit_intercept=True)
    reg_res=lm.fit(Y, res)
    #residual plot
    plt.scatter(Y, res, alpha=.5)
    plt.plot(Y, reg_res.predict(Y), color="red")
    plt.axhline(0, color='grey', linestyle='--')
    plt.xlabel('observed values of Yi')
    plt.ylabel('residuals, Yi-Y^')
    plt.title("residuals, RSS={:,.1f}".format(RSS))

#export coefficients strings for plt.plot
def coef_str(reg):
    coef=np.hstack([reg.intercept_, reg.coef_.ravel()])
    print(coef)
    #
    coef_list=['beta'+str(i)+'='+str(round(x,4)) for i,x in enumerate(coef)]
    coef_str="\n".join(coef_list)
    return coef_str

#10-fold cross validation
def cross_validation(X, Y, times=20):
    RSS=[]
    R2=[]
    for i in range(times):
        #split data
        X_train,X_test,Y_train,Y_test = \
        model_selection.train_test_split(X, Y, test_size=.1)
        #lm
        lm=linear_model.LinearRegression(fit_intercept=True)
        reg=lm.fit(X_train,Y_train)
        #residuals
        res=Y_test-reg.predict(X_test)
        #RSS
        RSS.append(np.sum(res**2))
        #R^2 coefficient correlation
        R2.append(reg.score(X_test, Y_test))
    
    #plot
    fig,(ax1, ax2)=plt.subplots(1,2)
    ax1.plot(RSS)
    ax1.axhline(np.median(RSS), color='black', linestyle='--')
    ax1.set_title("median-RSS={:,.0f}".format(np.median(RSS)))
    ax1.set_xlim(0,times)
    ax1.set_xlabel('Times')
    ax2.plot(R2)
    ax2.axhline(np.median(R2), color='black', linestyle='--')
    ax2.set_title("median-$R^2$={:,.4f}".format(np.median(R2)))
    ax2.set_xlim(0,times)
    ax2.set_xlabel('Times')
    fig.suptitle("10-fold corss validation")
    #
    return (RSS, R2)


#prediciton interval of coefficients using bootstrapping
def prediction_interval(X, Y, times=100, t=1.96):
    coefs_num=len(list(X))
    coefs=np.zeros(shape=(times,len(list(X))))
    coefs.shape
    for i in range(times):
        #split data
        X_train,X_test,Y_train,Y_test = \
        model_selection.train_test_split(X, Y, test_size=.1)
        #lm
        lm=linear_model.LinearRegression(fit_intercept=True)
        reg=lm.fit(X_train,Y_train)
        #
        coefs[i]=reg.coef_.ravel()
    #
    PI=pd.DataFrame({'index': np.arange(len(list(X))),
        'mean': coefs.mean(axis=0), 'std':coefs.std(axis=0),
       'lower':coefs.mean(axis=0)-t*coefs.std(axis=0),
       'upper':coefs.mean(axis=0)+t*coefs.std(axis=0)},
       index=list(X))
    #plot
    fig,ax=plt.subplots(1,1,figsize=(12,6))
    PI.plot.bar(PI.index, 'mean', rot=45, legend=False,
        yerr=2*PI["std"],color='lightgrey', ax=ax,
        title="95% Prediction intervals")
#    ax.errorbar(PI.index, PI['mean'], yerr=2*PI["std"],
#                linewidth=2, color='black', capsize=5)
    #ax.lines[0].remove()
    plt.axhline(0, c='grey')
    plt.ylabel("mean of coefficients")
 
    return PI
