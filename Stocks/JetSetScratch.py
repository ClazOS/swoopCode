# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 21:58:36 2014

@author: swoop
"""
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from zipline.utils.factory import load_bars_from_yahoo
start = datetime.datetime(2010,1,18)
end = datetime.datetime.today()

X = {
   0: ('TVIX', '10/07/2014'),
#   1: ('COST', '2/5/2002'),
#   2: ('CHK', '12/1/1994'),
#   3: ('HAS', '2/20/2013'),
#   4: ('INTC', '3/12/2012'),
#   5: ('GMCR', '2/20/2013'),
#   6: ('CRM', '12/12/2005'),
#   7: ('VRTX', '8/26/2013'),
#   8: ('DPM', '12/12/2012'),
#   9:('YHOO', '8/14/2002'),
#   10:('GOOGL', '6/24/2005'),
#   11:('FCX', '3/4/2004'),
}
purchases = pd.DataFrame({i:(X[i][0], pd.to_datetime(pd.Timestamp(X[i][1], tz='utc')))
                         for i in X}).T

purchases.columns = columns=['symbol','Date']
data = load_bars_from_yahoo(stocks=purchases.symbol)
prices = data.minor_xs('price')
prices

def thing(days_back, days_ahead):
    data = {}
    delta = datetime.timedelta
    for i in purchases.index:
        ticker, dt = purchases.ix[i]
        before = dt - delta(days=days_back)
        after = dt + delta(days=days_ahead)
        data[i] = prices[ticker].truncate(before=before, after=after).dropna()
    return data
       
   
truncated = thing(0, 365)
fig, axes = plt.subplots(len(truncated)+1, 1, figsize=(12,5*len(truncated)))
for i in truncated:
    
    axes[i].plot(truncated[i])
    axes[i].set_title(purchases['symbol'][i])

total=0.0
for i in truncated:   
    x = truncated[i]
    try:
        print purchases['symbol'][i], 'Percent Change:', str(round(np.log(x[-1]/x[0])*100,2))+'%'
        total+=np.log(x[-1]/x[0])
    except:
        pass

print 'Average Growth:',str(round(total*100/len(truncated),2))+'%'
    

    