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
i = np.arange(81).reshape(9,9)
value = dat['value']
qT2 = dat['qT2']
delta = dat['delta']
xClas=range(len(xBin)-1)
Q2Clas=range(len(Q2Bin)-1)
zClas=range(len(zBin)-1)
ind = np.arange(336)

dat['xClas'] = pd.cut(dat['x'], xBin, labels=False)
dat['xBin'] = pd.cut(dat['x'], xBin,labels = False, retbins=0)
xBind = dat['xClas']
xBinned = pd.DataFrame({'xBin': dat['xBin']},index = ind)

dat['Q2Clas'] = pd.cut(dat['Q2'], Q2Bin, labels=False)
dat['Q2Bin'] = pd.cut(dat['Q2'], Q2Bin,labels = False, retbins=0)
Q2Bind = dat['Q2Clas']
Q2Binned = pd.DataFrame({'Q2Bin' : dat['Q2Bin']}, index = ind)

dat['zClas'] = pd.cut(dat['z'], zBin, labels=False)
dat['zBin'] = pd.cut(dat['z'], zBin,labels = False, retbins=0)
zBind = dat['zBin']
zBinned = pd.DataFrame({'zBin' : dat['zBin']}, index = ind)
data_binvalue = dat['value'].as_matrix(columns=None)
data_binqT2 = dat['qT2'].as_matrix(columns=None)
data_bindelta = dat['delta'].as_matrix(columns=None)
data_binz = dat['z'].as_matrix(columns=None)
data_binx = dat['x'].as_matrix(columns=None)

# Creates the index needed to create f and g DataFrames
ind = np.arange(336)
Gridmap = np.arange(80)

X = dat['pT']

h = {'xBin': xBind, 'Q2Bin': Q2Bind, 'zBin' : zBind}
# Creates a DataFrame with qT2 as x, value as y
g = pd.DataFrame({'x': data_binx, 'value': data_binvalue, 'z' : data_binz, 'delta' : data_bindelta, 'qT2' :
    data_binqT2},index=ind)
xbin0 = xBinned.query('xBin == 0')
x0ind  = xbin0.index.values
new_xbin0 = X.iloc[x0ind]
xbin1 = xBinned.query('xBin == 1')
x1ind  = xbin1.index.values
new_xbin1 = X.iloc[x1ind]
xbin2 = xBinned.query('xBin == 2')
x2ind  = xbin2.index.values
new_xbin2 = X.iloc[x2ind]
xbin3 = xBinned.query('xBin == 3')
x3ind  = xbin3.index.values
new_xbin3 = X.iloc[x3ind]
xbin4 = xBinned.query('xBin == 4')
x4ind  = xbin4.index.values
new_xbin4 = X.iloc[x4ind]
xbin5 = xBinned.query('xBin == 5')
x5ind  = xbin5.index.values
new_xbin5 = X.iloc[x5ind]
xbin6 = xBinned.query('xBin == 6')
x6ind  = xbin6.index.values
new_xbin6 = X.iloc[x6ind]
xbin7 = xBinned.query('xBin == 7')
x7ind  = xbin7.index.values
new_xbin7 = X.iloc[x7ind]
xbin8 = xBinned.query('xBin == 8')
x8ind  = xbin8.index.values
new_xbin8 = X.iloc[x8ind]

# x axis label is pT for xbin
# y axis label is value for Q2 bin

xind = {'0':x0ind,'1':x1ind,'2':x2ind,'3':x3ind,'4':x4ind,'5':x5ind,'6':x6ind,'7':x7ind,'8':x8ind}

#Here is binned data for pT back in a DataFrame 
pTdat = pd.DataFrame({'0':new_xbin0,'1':new_xbin1,'2':new_xbin2,'3':new_xbin3,
                        '4':new_xbin4,'5':new_xbin5,'6':new_xbin6,'7':new_xbin7,
                        '8':new_xbin8},index = ind)
pTdatmod = pd.DataFrame({'0':new_xbin0,'1':new_xbin2,'2':new_xbin3,'3':new_xbin5,'4':new_xbin6,'5':new_xbin8},index = ind)    
valueind = pd.DataFrame({})                        
Y = dat['value']

joke = np.arange(0,9)
for value in joke:
    i = value
    q2binned = Q2Binned.query('Q2Bin == '+str(i))
    q2ind = q2binned.index.values
    valueind={str(i) : q2ind}
    
Q2bin0 = Q2Binned.query('Q2Bin == 0')
q0ind  = Q2bin0.index.values
value0 = Y.iloc[q0ind]
Q2bin1 = Q2Binned.query('Q2Bin == 1')
q1ind  = Q2bin1.index.values
value1 = Y.iloc[q1ind]
Q2bin2 = Q2Binned.query('Q2Bin == 2')
q2ind  = Q2bin2.index.values
value2 = Y.iloc[q2ind]
Q2bin3 = Q2Binned.query('Q2Bin == 3')
q3ind  = Q2bin3.index.values
value3 = Y.iloc[q3ind]
Q2bin4 = Q2Binned.query('Q2Bin == 4')
q4ind  = Q2bin4.index.values
value4 = Y.iloc[q4ind]
Q2bin5 = Q2Binned.query('Q2Bin == 5')
q5ind  = Q2bin5.index.values
value5 = Y.iloc[q5ind]
Q2bin6 = Q2Binned.query('Q2Bin == 6')
q6ind  = Q2bin6.index.values
value6 = Y.iloc[q6ind]
Q2bin7 = Q2Binned.query('Q2Bin == 7')
q7ind  = Q2bin7.index.values
value7 = Y.iloc[q7ind]
Q2bin8 = Q2Binned.query('Q2Bin == 8')
q8ind  = Q2bin8.index.values
value8 = Y.iloc[q8ind]
#Here is binned data for value back in a DataFrame 
valuedat = pd.DataFrame({'0':value0,'1':value1,'2':value2,'3':value3,
                        '4':value4,'5':value5,'6':value6,'7':value7,
                        '8':value8},index=ind)
valuedatmod = pd.DataFrame({'0':value0,'1':value2,'2':value3,'3':value6,
                        '4':value8},index=ind)
# I didnt use vdat in the end I used valuedat
vdat = {'0':value0,'1':value1,'2':value2,'3':value3,
                        '4':value4,'5':value5,'6':value6,'7':value7,
                        '8':value8}

    
Z = dat['z']
zbin0 = zBinned.query('zBin == 0')
z0ind  = zbin0.index.values
z0 = Z.iloc[z0ind]
zbin1 = zBinned.query('zBin == 1')
z1ind  = zbin1.index.values
z1 = Z.iloc[z1ind]
zbin2 = zBinned.query('zBin == 2')
z2ind  = zbin2.index.values
z2 = Z.iloc[z2ind]
zbin3 = zBinned.query('zBin == 3')
z3ind  = zbin3.index.values
z3 = Z.iloc[z3ind]
zbin4 = zBinned.query('zBin == 4')
z4ind  = zbin4.index.values
z4 = Z.iloc[z4ind]
zbin5 = zBinned.query('zBin == 5')
z5ind  = zbin5.index.values
z5 = Z.iloc[z5ind]

z = {'0':z0ind,'1':z1ind,'2':z2ind,'3':z3ind,'4':z4ind,'5':z5ind}
zdat = pd.DataFrame({'0':z0,'1':z1,'2':z2,'3':z3,'4':z4,'5':z5})
k = 0
num = 486
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
                num -= 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
             
            #if ydat.empty or xdat.empty:
            #    pass
            # else:
            #if len(databin['y']) != len(databin['x']):
            #    pass
            #else:
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
                   
            ax.grid()
                    
ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
ax.set_xlabel(r"$x$ bins")

databin = pd.DataFrame({})
fig2=py.figure(figsize=(15, 15),facecolor="gray")
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
                num -= 1
                pass
            else:
                print('xbin = ' + str(f))
                print('ybin = ' + str(j))
                print('k = ' + str(k))
                print('bin'+ str(i))
                print(databin)
             
            #if ydat.empty or xdat.empty:
            #    pass
            # else:
            #if len(databin['y']) != len(databin['x']):
            #    pass
            #else:
            ax.errorbar(databin['x'],databin['y'],yerr=databin['d'],capsize=6,linestyle="")
            ax.set_yscale("log")
                   
            ax.grid()
                    
ax.set_ylabel(r"$Q^2$ bins",rotation="horizontal")
ax.set_xlabel(r"$x$ bins")
fig3=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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
            ax.grid()
fig4=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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
            ax.grid()   
fig5=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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
fig6=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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
fig7=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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
fig8=py.figure(figsize=(10, 10),facecolor="gray")
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
                num -= 1
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