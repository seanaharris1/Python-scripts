# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:25:55 2016

@author: SHarris
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 10:22:10 2016

@author: SHarris
"""

import requests
import time 
import datetime
from requests.auth import HTTPBasicAuth
import pylab as plt
import numpy as np
import matplotlib
import math
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import matplotlib.animation as animation
import ssl


class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)
                                              
todaydate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
symbols_list = ['AAPL','GOOG','EMR','VSLR','LEDS','VRX','WATT']
boughtdict = {'AAPL':[170],
          'GOOG':[700],
          'EMR':[50],
          'VSLR':[3],
          'LEDS':[5],
          'VRX':[28],
'WATT':[18]}
quantboughtdict = {'AAPL':[10],
                   'GOOG':[5],
                    'EMR':[100],
                    'VSLR':[300],
                    'LEDS':[40],
                    'VRX':[50],
                    'WATT':[40]}
boughtGOOG = [700]
boughtAAPL = [170]
boughtVLSR = [3]
boughtLEDS = [6]
boughtEMR = [50]
boughtWATT = [10]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def realtime():
    for symbol in symbols_list:
        """ code for scraping stock data from yahoo. 
        reference http://www.jarloo.com/yahoo_finance/ for more info """
        textfile = 'stockdatatest'+todaydate+symbol+'.txt'
        with open(textfile,'a') as textfile:
            #symbolname = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s=".join(secondhalf),\
            #auth = HTTPBasicAuth('user','pass')).text
            urlrequest = "https://download.finance.yahoo.com/d/quotes.csv?s="+symbol+"&e=.csv&f=l1opv"
            symbolname = requests.get(urlrequest,verify=True, \
            auth = HTTPBasicAuth('seanharris1120','astro33029')).text 
            #code for pulling the stock information from yahoo
            list1 = symbolname.split(",") 
            #splitting the string into a list, making a new element after every comment 
            ts = time.time() 
            #timestamp in unix form
            time_format = '%Y-%m-%d %H:%M:%S.%f'        
            st = datetime.datetime.fromtimestamp(ts).strftime(time_format) 
            #converting unix timestamp to readable timestamp
            print symbol,st,symbolname
            list1.append(st) #adding time to list of stock information
            #print list1[1]
                
            textfile.write(symbol+','+st+','+symbolname)
               

            lasttradedict = {}
            opdict = {}
            closedict = {}
            volumedict = {}
            timedict = {}
            symdict = {}
            
            """ making list using dictionary """
            for i in symbols_list:
                symdict['symlist_%s' % i] = []
                lasttradedict['lasttradelist_%s' % i] = []
                opdict['oplist_%s' % i] = []
                closedict['closelist_%s' % i] = []
                volumedict['volumelist_%s' % i] = []
                timedict['timelist_%s' % i] = []
                
            #print symdict
            
            with open('stockdatatest'+todaydate+symbol+'.txt','r') as textfile:
                lines = textfile.readlines()
                #print lines
                """ for loop to split the string and append to appropriate
                lists for analysis """
                for line in lines:
                    #line.replace('"','')
                    sym,time1,lasttrade,op,close,volume = line.replace("\n","").split(",")
#                    namelist.append(name)
                    symdict['symlist_'+i].append(sym)
                    lasttradedict['lasttradelist_'+i].append(lasttrade)
                    opdict['oplist_'+i].append(op)
                    closedict['closelist_'+i].append(close)
                    volumedict['volumelist_'+i].append(volume)
                    timedict['timelist_'+i].append(time1)
                
                    
                    """ converting dates to numbers for plotting, then plotting
                    time vs. last trade """
               
                    newdates = matplotlib.dates.datestr2num(timedict['timelist_'+i])
                    realtime.newdates = newdates
                    realtime.lasttrade = lasttradedict['lasttradelist_'+i]
                    
            
                    #plt.plot_date(newdates,lasttradelist)

                    #dictionary+i == dict(zip(timelist,lasttradelist))
                    #print dictionary+i
            

            
            #for key in bought.iterkeys():
            
            """ making new list for latest trade to make it easier to implement
            the live graph 08/04/2016 """

                    #realtime.newdates = newdates
                    
            with open('lasttradefile'+todaydate+symbol+'.txt','w') as newfile:
                lasttrade = lasttradedict['lasttradelist_'+i]
                newfile.write('\n'.join(lasttrade))
#            for i in symbols_list:
#                print bought.get(i)
            #print line    
            #print lasttradelist
            #print len(lasttradelist)
#            for i in lasttradelist:
#                newint = int(float(i))
            if len(lasttradedict['lasttradelist_'+i]) > 2:
                    (opdict['oplist_'+i][2]) 
                    #print float(lasttradedict['lasttradelist_'+i][-1])-
                    #print (boughtdict['boughtlist_'+i][0])

        """ comparing the bought price to the most recent trade 08/12/2016 """
        if len(lasttradedict['lasttradelist_'+i]) >2:
            currenttrade = float(lasttradedict['lasttradelist_'+i][-1])
            bought = (boughtdict[symbol])[0]
            singleprofit = currenttrade - bought
            boughtquant = quantboughtdict[symbol][0]
            tenpercent = float((currenttrade*0.10*boughtquant) - \
            bought*0.10*boughtquant)  
            print currenttrade
            print bought
            print "%s price has increased by %s" % (symbol, singleprofit)
            print "if you sold 10 percent of %s stocks bought at $%s, profit will be $%s" % (symbol, bought, tenpercent)
    time.sleep(10) 
    #running the loop every 5 seconds, put outside the loop so every symbol
    # in the list runs in the loop, not 1 every 5 seconds 

#X = np.linspace(0,2,1000)
#Y = X**2 + np.random.random(X.shape)
data = np.loadtxt('lasttradefile2016-08-04AAPL.txt',unpack = True)
#graph = plt.plot(X,Y)[0]
while True:
    for i in symbols_list:
        realtime()
#        x = realtime.newdates
#        plt.plot_date(x,realtime.lasttrade,ls='-',marker='o')
        
    #plt.plot(x,y,label="test file")
    #plt.xlabel('x')
    #plt.ylabel('y')
    #plt.title('test')
    #graph.set_ydata(Y)
#        plt.ion()
#        plt.draw()
#        plt.pause(0.01)
    
    
s = requests.Session()
s.mount('https://',MyAdapter())
s.get('https://download.finance.yahoo.com/d/quotes.csv?s=AAPL&e=.csv&f=nsl1opv')    
t = requests.get('https://download.finance.yahoo.com/d/quotes.csv?s=AAPL&e=.csv&f=nsl1opv')
t.text