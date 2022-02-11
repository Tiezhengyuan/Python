# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:02:11 2017

@author: yuan
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

if __name__=='__main__':
    #read data frmae
    infile='/home/yuan/results_phip/phipseq6_human/statistics/lowRC_pep_scalingRC.txt'
    indf=pd.read_csv(infile,sep='\t', index_col=0)
    indf.shape
    
    #observe the data
    NC_median=indf.ix[:,0:8].apply(median, axis=1)
    NC_std=indf.ix[:,0:8].apply(std, axis=1)
    NC=pd.DataFrame({'median':NC_median,'std':NC_std})
    
    #
    formula='std~median'
    model=smf.ols(formula, data=NC)
    results=model.fit()
    print results.summary()    
    #predict values of dependentable variables based on the fitted model
    NC['pred_std']=results.predict()

    
    #methods1: Residuals analysis
    #residuals: difference between observed values and the fitted line
    NC['residual']=NC['std']-NC['pred_std']
    std_res=np.std(NC['residual'])
    print "STD of residuals=", std_res
    print 'Mean of residuals', np.mean(NC['residual'])
    NC['standarized_residual']=(NC['residual']-np.mean(NC['residual']))/std_res
    
    #Good fit should show a farily random pattern
    #residual plot
    plt.clf()
    plt.ylim(-10,10)
    plt.plot(NC['median'], NC['standarized_residual'], 'b.')#observed
    plt.text(40,8,  'std(res)='+str(std_res))
    plt.axhline(y=np.mean(NC['residual']), color='grey')
    plt.xlabel('explanatory variable:median')
    plt.ylabel('Standarized Residuals')
    plt.show()
    
    #quantile of residual
    med_frq=pd.DataFrame(NC['median'].value_counts())
    med_frq=med_frq.iloc[:50,]
    med_frq=med_frq.reindex(sort(list(med_frq.index)))
    a=list()
    b=list()
    c=list()
    for i in list(med_frq.index):
        sub_res=NC.loc[NC['median']==i,'standarized_residual']
        a.append(np.percentile(sub_res,.25))
        b.append(np.percentile(sub_res,.5))
        c.append(np.percentile(sub_res,.75))
    med_frq['25']=a
    med_frq['50']=b
    med_frq['75']=c
    #present the fitting model
    plt.clf()
    plt.plot(list(med_frq.index), med_frq['25'], 'r-')
    plt.plot(list(med_frq.index), med_frq['50'], 'b-')
    plt.plot(list(med_frq.index), med_frq['75'], 'g-')
    plt.xlabel('Median')
    plt.ylabel('Standarized residual')
    plt.title('Quantiles of residuals')
    plt.show()
    
    

    print 'ok'