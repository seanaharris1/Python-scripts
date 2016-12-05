# -*- coding: utf-8 -*-
"""
Created on Mon May 23 12:34:48 2016

@author: SHarris
"""

import pandas as pd
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol
import sympy as sp
from matplotlib.backends.backend_pdf import PdfPages


symbols_list = ['IBM','GOOG', 'MSFT','GE','VSLR','ELS','EMR',
                'LEDS','VRX','WATT']
d = {}
for ticker in symbols_list:
    try:
        d[ticker] = DataReader(ticker, "yahoo", '2016-05-10')
    except:
        pass
           
pan = pd.Panel(d)
df1 = pan.minor_xs('Adj Close')
df4 = pan.minor_xs('Volume')
#datevalues = df1.index.values

"""
    saving local copy of the dataframe using pickle to allow for faster 
    running speed and avoiding error from broken URL
"""

df1.to_pickle("C:\Users\sharris\Documents\Python Scripts\stockdf.pkl")
df4.to_pickle("C:\Users\sharris\Documents\Python Scripts\stockvolumedf.pkl")
df5 = pd.read_pickle("C:\Users\sharris\Documents\Python Scripts\stockvolumedf.pkl")
df2 = pd.read_pickle("C:\Users\sharris\Documents\Python Scripts\stockdf.pkl")
df3 = df2.copy()
df2.reset_index(level=0,inplace=True) #making the date index into a column
df2.index = df2.index + 1
#print df2.describe() #pulling mean, high, low of each column
df6 = df5.copy()
df5.reset_index(level=0,inplace=True)
df5.index = df5.index +1
dates = df2['Date'] #date column
#tesladf = df2[['Date','TSLA']]
#print tesladf
#tesladfplot = df3['TSLA'] #dataframes used for plots must have date as index
googdf = df2[['Date','GOOG']]
ibmdf = df2[['Date','IBM']]
microsoftdf = df2[['Date','MSFT']]
googdf.mean()
#teslamrv=tesladf.iloc[-1:]['TSLA'] # prints the most recent value = mcv
x = Symbol('x')
#%% cell for percent change function
""" function for finding percent change of giving stock symbol, must be string  """
def percentchange(sym2):
    for sym in sym2:
        symdf = df2[['Date',sym]]
        symmrv = symdf.iloc[-1:][sym]
        symavg = symdf[-10:].mean()[0]
        symchange = (symmrv.max()-symavg)/symavg*100
        tendayavg = symdf[-10:].mean()[0]
        """ code for plotting the adjusted close line graph with date as y-axis """
        figname = sym +' report.pdf'
        
        symplot = df3[sym]
        symplot.to_frame()
        plt.plot(df3.index.to_pydatetime(),df3[sym])
      
        plottitle = sym+' Adjusted Close over time'
        plt.title(plottitle)
        fig = plt.gcf()
        plt.show()
        
        
        """ code for regressing adjusted close data to a 4th degree polynomial 
        and plotting that polynomial regression against a scatter plot of the 
        adjusted close values """
        
        xdata = range(0,len(symplot.values),1)
        symregression = np.polyfit(xdata,symplot,4)
        poly = np.poly1d(symregression)
        ydata = poly(xdata)
        polyeq = symregression[0]*x**4 + symregression[1]*x**3 + symregression[2]*x**2 \
        + symregression[3]*x + symregression[4]
        #deriv = sp.diff(polyeq,x)
        #roc = deriv.subs(x,len(xdata)) #roc = rate of change
        #roc = (symmrv-symdf.iloc[-10][sym].max()/symdf.iloc[-10][sym])
       
        
        plt.plot(xdata,symplot,'o',label = 'Actual Adjusted Close')
        plt.plot(xdata,ydata,'-',label = 'adjusted close regressed curve')
        regressplottitle = sym+' Adjusted Close Actual vs Predicted'
        plt.title(regressplottitle)
        lgd = plt.legend(loc = 'upper center',bbox_to_anchor = (0.5,-0.1))
        fig = plt.gcf()
        plt.show()
        plt.draw()
        figname = sym +' report'
        #fig.savefig(figname,bbox_extra_artists=(lgd,), bbox_inches ='tight')
        
        
        """ code for program feedback for telling user if the stock's most recent
        adjusted close has increased or decreased compared to the average 
        adjusted close over the past 10 days """
        
        print sym,'closed at $',symmrv,'in the most recent closing day'
        if symchange < 0:
            print sym, "adjusted close yesterday dropped",symchange, \
            "% compared to the average adjusted close over the past 10 days"
        if symchange > 0:
            print sym, "adjusted close yesterday rose",symchange, \
            "% compared to the average adjusted close over the past 10 days"
            
        """ volume data pull and volume percent change """
        #print 'the rate of change is $',roc, 'today'
        print sym,'10 day average is $',tendayavg
        voldf = df5[['Date',sym]]
        volmrv = voldf.iloc[-1:][sym]
        symtwodaysago = symdf.iloc[-2][sym]
        volumechange = (volmrv - symtwodaysago)/symtwodaysago
        
        """ volume plot """
        
        symplot = df6[sym]
        symplot.to_frame()
        plt.plot(df6.index.to_pydatetime(),df6[sym])
        plt.title(sym+' Volume over time')
        plt.show()

#%%        
percentchange(symbols_list)
#teslachange = (teslamrv.max()-teslamean)/teslamean*100

#(teslamrv.max()-teslamean)/teslamean*100, '%' # finds the percent
#xaxis = date2num(df1['Date'])
#tesladfplot.to_frame()
#tesladfplot.plot(kind='line')
#plt.title('Tesla Adjusted Close over time')
#plt.show()
#teslavalues = tesladfplot.values
#teslalist = []
#for x in teslavalues:
#    teslalist.append(x)
#xaxis = range(0,len(teslalist),1)
#xaxis2 = len(xaxis)+1
""" fitting the data to a 4th degree polynomial and plotting it against the 
actual data. add legend and extrapolate data to predict future value 05/31/16"""

#teslareg = np.polyfit(xaxis,teslalist,4)
#teslareg
#polynomial = np.poly1d(teslareg)
#ys = polynomial(xaxis)
#plt.plot(xaxis,teslalist,'o',label = 'actual adjusted close')
#plt.plot(xaxis,ys,label = 'predicted adjusted close')
#plt.legend(loc='upper left')
#plt.title('Tesla Adjusted Close')
#plt.show()
x = Symbol('x')
#x=len(teslalist)+1
#teslaeq =  teslareg[0]*x**4 + teslareg[1]*x**3 + teslareg[2]*x**2 + teslareg[3]*x+teslareg[4]    
#diff = sp.diff(teslaeq,x)
#diffeval = sp.diff.subs(x,21)
#print teslaeq.subs(x,26)
#print sp.diff(x,26)
#print teslaeq
#print teslamrv
""" difference of the most recent days adjusted close value and the mean 
    adjusted close value of the previous 10 days. May add function to do percent 
    difference for other time periods i.e. 30 days, 1 year, etc """



""" make plots showing adjusted close data 05/23/2016 """