# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:36:02 2022

@author: Winggy Wu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import interpolate

def bin_data(data, xname, yname, bins=30, agg_fn=np.nanmedian):
    hist, edges = np.histogram(data[xname], bins=bins)
    bin_midpoint = np.zeros(edges.shape[0]-1)
    binned_df = pd.DataFrame(np.zeros((edges.shape[0]-1, 1)))
    for i in range(edges.shape[0]-1):
        bin_midpoint[i] = (edges[i] + edges[i+1]) / 2
        if i < edges.shape[0]-2:
            dat_temp = data.loc[(data[xname] >= edges[i]) & (
                data[xname] < edges[i+1]), :]
        else:
            dat_temp = data.loc[(data[xname] >= edges[i]) & (
                data[xname] <= edges[i+1]), :]
        binned_df.loc[binned_df.index[i], xname] = bin_midpoint[i]
        binned_df.loc[binned_df.index[i], yname] = agg_fn(dat_temp[yname])
       
    return binned_df

data=pd.read_csv(r'.\datasample\test2_para.csv')
data=data[~(data['NDVI']<0.1)]
data['Temp']=data['Temp']-273.15
data=data[data['Temp']>0]
XY = bin_data(data,'SWR','Rchl').dropna()
X0=XY['SWR'].values
Y0=XY['Rchl'].values
if(Y0.shape[0]>13):    
    Ys0=signal.savgol_filter(Y0, 13, 3)
    
    f=interpolate.interp1d(X0, Ys0, kind='quadratic')
    X=np.arange(int(np.nanmin(X0)+1),int(np.nanmax(X0)))
    Ys=f(X)        

    peaks=signal.argrelextrema(Ys, np.greater, order=10)
    peak_ind=peaks[0]
    peak_ind=peak_ind[peak_ind>100]
    fig,ax=plt.subplots()
    ax.scatter(X0,Y0,color='blue')
    ax.plot(X,Ys,color='black')
    ax.scatter(X[peak_ind],Ys[peak_ind],marker='o',color='red',label='peaks')
    ax.set_xlabel('SWR')
    ax.set_ylabel('Rchl')
    fig.savefig(r'.\fig\test2.png')
    if(peak_ind.shape[0]>0):            
        peak_max=Ys[peak_ind]
        thr_candidate=np.argmax(peak_max)
        if ((Ys[peak_ind[thr_candidate]]>=Ys[-1])&(peak_ind[thr_candidate]>3)):
            thr=X[peak_ind[thr_candidate]]
