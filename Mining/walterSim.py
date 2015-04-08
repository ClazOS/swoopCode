# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:46:36 2014

@author: swoop
"""

###Walter
def machinesPriceDay(siteProdHour,mCostPerHour,hours=12,): 
    machineCostPerDay=mCostPerHour*hours
    numMachines=siteProdHour/40
    return machineCostPerDay*numMachines
    
def priceList():
    prod200=[]
    prod225=[]
    prod250=[]   
    for i in xrange(80,320):
        prod200.append(machinesPriceDay(i,200))
        prod225.append(machinesPriceDay(i,225))
        prod250.append(machinesPriceDay(i,250))
    plt.plot(prod200,'r',prod225,'g',prod250,'b')
    plt.title('$/Hour for Hourly Production')
    plt.legend(('Daily Cost At 200 s./','Daily Cost At 225 s./','Daily Cost At 250 s./'),'best')
    plt.xlabel('Production Per Hour')
    plt.ylabel('S./ Per Hour')
    plt.show()
    plt.plot(prod250)
    plt.show()
