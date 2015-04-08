# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:44:17 2014

@author: swoop
"""

def fracbig(numer,denom,its):
    while its>0:
        for i in xrange(its):
            denom=denom+numer
            print str(numer)+'/'+str(denom)
    
            
    