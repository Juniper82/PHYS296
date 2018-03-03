# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:21:39 2018

@author: Dolam
"""
# I may be flying south when Im supposed to be flying north.....Should I turn around???
import pandas as pd
import numpy as np
from matplotlib import pyplot as py
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
# enable plots in the notebook
#%matplotlib inline
#cc = pd.read_excel('CustomColors.xlsx')
dat=pd.read_excel('C:/Users/Dolam/Documents/Scott/1000.xlsx');

# Calculate 
dat["delta"] = np.sqrt(dat["stat_u"]**2.0) #measurment error
dat["qT"] = dat["pT"]/dat["z"]
dat["qT2"] = dat["qT"]**2

##Binning data Tick marks for overall 9x9 matrix
xBin=np.array([0.023,0.04,0.055,0.075,0.1,0.14,0.2,0.3,0.4,0.6]) 
Q2Bin=np.array([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 3.0, 5.0, 15.0])
zBin= np.array([0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.1])

# creates index values for final plot matrix

ind = np.arange(336)
dat['xBin'] = pd.cut(dat['x'], xBin,labels = False, retbins=0)
xBinned = pd.DataFrame({'xBin': dat['xBin']},index = ind)
dat['Q2Bin'] = pd.cut(dat['Q2'], Q2Bin,labels = False, retbins=0)
Q2Binned = pd.DataFrame({'Q2Bin' : dat['Q2Bin']}, index = ind)
dat['zBin'] = pd.cut(dat['z'], zBin,labels = False, retbins=0)
zBinned = pd.DataFrame({'zBin' : dat['zBin']}, index = ind)

# Creates the index needed to create f and g DataFrames
ind = np.arange(336)
X = dat['pT']
Y = dat['value']
delta = dat['delta']

joke = np.arange(0,9)
PTbinned = {'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind,'6':ind,'7':ind,'8':ind}
valuebinned = {'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind,'6':ind,'7':ind,'8':ind}
for value in joke:
    i = value
    xBin = xBinned.query('xBin == '+str(i))
    xindex = xBin.index.values
    PTbinned[str(i)]=X.iloc[xindex]
    q2binned = Q2Binned.query('Q2Bin == '+str(i))
    q2ind = q2binned.index.values
    valuebinned[str(i)]=Y.iloc[q2ind]
# x axis label is pT for xbin
# y axis label is value for Q2 bin

#Here is binned data for pT back in a DataFrame 
pTdat = pd.DataFrame({'0':PTbinned['0'],'1':PTbinned['1'],'2':PTbinned['2'],'3':PTbinned['3'],
                        '4':PTbinned['4'],'5':PTbinned['5'],'6':PTbinned['6'],'7':PTbinned['7'],
                        '8':PTbinned['8']},index = ind)
pTdatmod = pd.DataFrame({'0':PTbinned['0'],'1':PTbinned['2'],'2':PTbinned['3'],'3':PTbinned['5'],
                         '4':PTbinned['6'],'5':PTbinned['8']},index = ind) 

valuedat = pd.DataFrame({'0':valuebinned['0'],'1':valuebinned['1'],'2':valuebinned['2'],
                            '3':valuebinned['3'],'4':valuebinned['4'],'5':valuebinned['5'],
                            '6':valuebinned['6'],'7':valuebinned['7'],'8':valuebinned['8']},index=ind)

valuedatmod = pd.DataFrame({'0':valuebinned['0'],'1':valuebinned['2'],'2':valuebinned['3'],'3':valuebinned['6'],
                        '4':valuebinned['8']},index=ind)   
jokes = np.arange(0,6)    
z={'0':ind,'1':ind,'2':ind,'3':ind,'4':ind,'5':ind}
Z = dat['z']
for value in jokes:
    i = value
    zBin = zBinned.query('zBin == '+str(i))
    zindex = zBin.index.values
    z[str(i)]=zindex
    
num = 0
databin = pd.DataFrame({})
fig1=py.figure(figsize=(15, 15),facecolor="gray")
for f in pTdat:       
    for j in valuedat:
        if j == '8':
            k = int(f) +1
        elif j == '7':
            k = 10 + int(f)
        elif j == '6':
            k = 19 + int(f)
        elif j == '5':
            k = 28 + int(f)
        elif j == '4':
            k = 37 + int(f)
        elif j == '3':
            k = 46 + int(f)
        elif j == '2':
            k = 55 + int(f)
        elif j == '1':
            k = 64 + int(f)
        elif j == '0':
            k = 73 + int(f)
        ax = py.subplot(9,9,k)
        for column in z.keys():
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdat[f].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedat[j].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
           
ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
ax.set_xlabel(r"$x$ bins")
print('\nThere were '+str(num)+' empty databins')      


fig2=py.figure(figsize=(15, 15),facecolor="gray")
num = 0
for f in pTdatmod:       
    for j in valuedatmod:
        if j == '4':
            k = int(f) +1
        elif j == '3':
            k = 7 + int(f)
        elif j == '2':
            k = 13 + int(f)
        elif j == '1':
            k = 19 + int(f)
        elif j == '0':
            k = 25 + int(f)
               
        ax = py.subplot(5,6,k)
        for column in z.keys():
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod[f].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod[j].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")                   
ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
ax.set_xlabel(r"$x$ bins")
print('\nThere were '+str(num)+' empty databins')
      
fig3=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod['0'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['0'].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 0 vs ybin 0')            
print('\nThere were '+str(num)+' empty databins')                  
            
fig4=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod['1'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['1'].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 2 vs ybin 2')           
print('\nThere were '+str(num)+' empty databins')      

fig5=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            
            xdat  = pTdatmod['2'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['2'].iloc[zindex]
            ydat = ydat.dropna()
           
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 3 vs ybin 3')           
            ax.grid()
print('\nThere were '+str(num)+' empty databins')      

fig6=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod['3'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['3'].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 5 vs ybin 6')            
            ax.grid()
print('\nThere were '+str(num)+' empty databins')      

fig7=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod['4'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['4'].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 6 vs ybin 8')            
            ax.grid()
print('\nThere were '+str(num)+' empty databins')      

fig8=py.figure(figsize=(10, 10),facecolor="gray")
num = 0
for column in z.keys():
            ax = py.subplot(1,1,1)
            i = column
            databin = pd.DataFrame({})
            zindex = z[i]
            xdat  = pTdatmod['5'].iloc[zindex]
            xdat = xdat.dropna()
            ydat = valuedatmod['4'].iloc[zindex]
            ydat = ydat.dropna()
            ddat = delta.iloc[zindex]
            ddat = ddat.dropna()                                                    
            databin = pd.DataFrame({'x':xdat,'y':ydat,'d':ddat})
            databin = databin.dropna()
            if databin.empty:
                num += 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
            
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
            py.title('xbin 8 vs ybin 8')       
            ax.grid()
print('\nThere were '+str(num)+' empty databins')      
pp = PdfPages('mod1000.pdf')
pp.savefig(fig1)
pp.savefig(fig2)
pp.savefig(fig3)
pp.savefig(fig4)
pp.savefig(fig5)
pp.savefig(fig6)
pp.savefig(fig7)
pp.savefig(fig8)
pp.close()