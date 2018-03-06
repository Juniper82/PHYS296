# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 10:04:07 2018

@author: JohnJohn
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as py
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
# enable plots in the notebook
#%matplotlib inline
#cc = pd.read_excel('CustomColors.xlsx')
#dat=pd.read_excel('C:/Users/Dolam/Documents/Scott/1000.xlsx');
dat=pd.read_excel('E:/Laptop/School/Interships/Dr_Prokudin/Juniper82/PHYS296/dat/expdat/1000.xlsx');

# Calculate 
dat["delta"] = np.sqrt(dat["stat_u"]**2.0) #measurment error
dat["qT"] = dat["pT"]/dat["z"]
dat["qT2"] = dat["qT"]**2

##Binning data Tick marks for overall 9x9 matrix
xBin=np.array([0.023,0.04,0.055,0.075,0.1,0.14,0.2,0.3,0.4,0.6]) 
Q2Bin=np.array([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 3.0, 5.0, 15.0])
zBin= np.array([0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.1])

# creates index values for final plot matrix

#ind = np.arange(336)
dat['xBin'] = pd.cut(dat['x'], xBin,labels = False, retbins=0)
#xBinned = pd.DataFrame({'xBin': dat['xBin']},index = ind) # xBinned = dat['xBin'].tolist()
dat['Q2Bin'] = pd.cut(dat['Q2'], Q2Bin,labels = False, retbins=0)
#Q2Binned = pd.DataFrame({'Q2Bin' : dat['Q2Bin']}, index = ind) # Q2Binned = dat['xBin']
dat['zBin'] = pd.cut(dat['z'], zBin,labels = False, retbins=0)
#zBinned = pd.DataFrame({'zBin' : dat['zBin']}, index = ind)
#
# Creates the index needed to create f and g DataFrames
#ind = np.arange(336)
#
#
#joke = np.arange(0,9)
#pTdat = pd.DataFrame({'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind,'6':ind,'7':ind,'8':ind},index = ind)
#valuedat = pd.DataFrame({'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind,'6':ind,'7':ind,'8':ind},index=ind)
#
#for value in joke:
#    i = value
#    xindex = xBinned.query('xBin == '+str(i)).index.values
#    pTdat[str(i)]=dat['pT'].iloc[xindex]
#    q2ind = Q2Binned.query('Q2Bin == '+str(i)).index.values
#    valuedat[str(i)]=dat['value'].iloc[q2ind]
#
#pTdatmod = pd.DataFrame({'0':pTdat['0'],'1':pTdat['2'],'2':pTdat['3'],'3':pTdat['5'],
#                         '4':pTdat['6'],'5':pTdat['8']},index = ind) 
#
#valuedatmod = pd.DataFrame({'0':valuedat['0'],'1':valuedat['2'],'2':valuedat['3'],'3':valuedat['6'],
#                        '4':valuedat['8']},index=ind)   
#jokes = np.arange(0,6)    
#z={'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind}
#
#for value in jokes:
#    i = value
#    zBin = zBinned.query('zBin == '+str(i))
#    zindex = zBin.index.values
#    z[str(i)]=zindex
#    
#num = 0
#
#fig1=py.figure(figsize=(15, 15),facecolor="gray")
## Set custom ticks
#ax=fig1.add_axes([0,0,1,1])
#ax.yaxis.set_ticks([0,0.023,0.04,0.055,0.075,0.1,0.14,0.2,0.3,0.4,0.6])
#ax.xaxis.set_ticks([0,1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 3.0, 5.0, 15.0])
#ax.set_yticklabels([0]+Q2Bin)
#ax.set_xticklabels([0]+xBin)
#ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
#ax.set_xlabel(r"$x$ bins")
#globalGrid=gridspec.GridSpec(1, 1, wspace=0.0, hspace=0.0) #the axis to put subplot grid in
#innerGrid=gridspec.GridSpecFromSubplotSpec(9, 9, subplot_spec=globalGrid[0], wspace=0.0, hspace=0.0) #subplot grid
#
#for f in pTdat:       
#    for j in valuedat:
#        if j == '8':
#            k = int(f) 
#        elif j == '7':
#            k = 9 + int(f)
#        elif j == '6':
#            k = 18 + int(f)
#        elif j == '5':
#            k = 27 + int(f)
#        elif j == '4':
#            k = 36 + int(f)
#        elif j == '3':
#            k = 45 + int(f)
#        elif j == '2':
#            k = 54 + int(f)
#        elif j == '1':
#            k = 63 + int(f)
#        elif j == '0':
#            k = 72 + int(f)
#        ax = fig1.add_subplot(innerGrid[k])
#        ax.set_yscale("log")
#        for column in z.keys():
#            xdat  = pTdat[f].iloc[z[column]].dropna()
#            ydat = valuedat[j].iloc[z[column]].dropna()
#            ddat = dat['delta'].iloc[z[column]].dropna()
#            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat}).dropna()
#            if databin.empty:
#                num += 1
#                ax.set_yticklabels('')
#                ax.set_xticklabels('')
#                pass
#            else:
#                print('xbin = ' + str(f))
#                print('ybin = ' + str(j))
#                print('k = ' + str(k))
#                print('bin'+ str(i))
#                print(databin)
#                ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
     
for f,F in zip(range(len(pTdatmod)),pTdatmod):       
    for j,J in zip(range(len(valuedatmod)),valuedatmod):

        print (j,f)
##############################
# for loop
forbinX = 0
forbinY = 0

maskX = dat['xBin'].isin([forbinX]) 
maskY = dat['Q2Bin'].isin([forbinY])
# apply our mask
datmod = dat[maskX & maskY]

# for loop
forbinZ = 0

maskZ = datmod["zBin"].isin([forbinX])
# apply our mask
pltdat = datmod[maskZ]
################################

###############
# HermesPlot ##
###############   
fig2=py.figure(figsize=(15, 15),facecolor="gray")
ax=fig2.add_axes([0,0,1,1])
ax.yaxis.set_ticks([0,0.023,0.04,0.055,0.075,0.1,0.14,0.2,0.3,0.4,0.6])
ax.xaxis.set_ticks([0,1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 3.0, 5.0, 15.0])
ax.set_yticklabels([0]+Q2Bin)
ax.set_xticklabels([0]+xBin)
globalGrid=gridspec.GridSpec(1, 1, wspace=0.0, hspace=0.0) #the axis to put subplot grid in
innerGrid=gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=globalGrid[0], wspace=0.0, hspace=0.0)
Zcolor=["red","green","blue","orange","purple","brown"]
Zmark=["o","o","o","o"]
#Zline=[':','-.','--','-']
Zpatch1 = mpatches.Patch(color=Zcolor[0], label='zbin 0')
Zpatch2 = mpatches.Patch(color=Zcolor[1], label='zbin 1')
Zpatch3 = mpatches.Patch(color=Zcolor[2], label='zbin 2')
Zpatch4 = mpatches.Patch(color=Zcolor[3], label='zbin 3')
Zpatch5 = mpatches.Patch(color=Zcolor[4], label='zbin 4')
Zpatch6 = mpatches.Patch(color=Zcolor[5], label='zbin 5')
ax.legend(handles=[Zpatch1,Zpatch2,Zpatch3,Zpatch4,Zpatch5,Zpatch6],loc='upper left')
ax.grid()
ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
ax.set_xlabel(r"$x$ bins")

pTdatmod=[0,2,3,5,6,8] # Q2bins that overlap xBins
valuedatmod=[0,2,3,6,8] # xBins that overlap Q2Bins
num = 0
for f,F in zip(range(len(pTdatmod)),pTdatmod):       
    for j,J in zip(range(len(valuedatmod)),valuedatmod):
        if j == 4:
            k = int(f) # kth possition for subplot on innerGrid matrix
            maskX = dat['xBin'].isin([J]) # retruns bolinan for all Jth xBin in dat  
            maskY = dat['Q2Bin'].isin([F]) # retruns bolinan for all Fth Q2Bin in dat
        elif j == 3:
            k = 6 + int(f)
            maskX = dat['xBin'].isin([J]) 
            maskY = dat['Q2Bin'].isin([F])
        elif j == 2:
            k = 12 + int(f)
            maskX = dat['xBin'].isin([J]) 
            maskY = dat['Q2Bin'].isin([F])
        elif j == 1:
            k = 18 + int(f)
            maskX = dat['xBin'].isin([J]) 
            maskY = dat['Q2Bin'].isin([F])
        elif j == 0:
            k = 24 + int(f)
            maskX = dat['xBin'].isin([J]) 
            maskY = dat['Q2Bin'].isin([F])
        ax = fig2.add_subplot(innerGrid[k]) # add subplot in innerGrid
        xydat = dat[maskX & maskY] # subset of data for Jth xBin and Fth Q2Bin
        for z in range(len(zBin)-1): 
            maskZ = xydat["zBin"].isin([z])
            databin = xydat[maskZ]
#            xdat  = pTdatmod[f].iloc[z[column]].dropna()
#            ydat = valuedatmod[j].iloc[z[column]].dropna()
#            ddat = dat['delta'].iloc[z[column]].dropna()
#            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat}).dropna()
            
            if databin.empty:
                num += 1
                ax.set_yticklabels('')
                ax.set_xticklabels('')
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
#                print('bin'+ str(i))
                print(databin)
                ax.errorbar(databin['pT'],databin['value'],yerr=databin['delta'],capsize=6,linestyle="")
                ax.set_yscale("log")                