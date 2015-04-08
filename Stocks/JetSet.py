# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 21:32:46 2014

@author: swoop
"""
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from zipline.utils.factory import load_bars_from_yahoo

class symbols(list):
   def __init__(self, *args):
       super(symbols, self).__init__(args)
       
   def get_data(self, start, end=None):
       if end is None:
            end = pd.Timestamp.utcnow()
       return load_bars_from_yahoo(stocks=self,
                                   start=pd.Timestamp(start, tz='utc'),
                                   end=pd.Timestamp(end, tz='utc'))

get_returns = lambda x: np.log(x / x.shift(1))    
compound = lambda x: (1 + x).cumprod()
rolling_compound = lambda x: compound(x)[-1]

syms = symbols('XIV', 'UVXY')
prices = syms.get_data('2014-01-01').minor_xs('price').dropna()

R = get_returns(prices)

xiv = pd.rolling_apply(R.XIV, 5, rolling_compound)
uvxy = pd.rolling_apply(-R.UVXY * 0.5, 5, rolling_compound)

spread = uvxy - xiv
spread.plot(figsize=(12,8))

compoundR = pd.DataFrame(dict(
   XIV=compound(R.XIV),
   UVXY=compound(-0.5*R.UVXY),
))
compoundR.plot()

spread = -R.UVXY / 2 - R.XIV
spread.plot(figsize=(15,10))

compound(spread).plot(figsize=(15,10))