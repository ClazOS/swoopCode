# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 18:03:30 2014

@author: swoop
"""
import random
import pylab

def stdDev(X):
    mean=sum(X)/float(len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5
    
def runTrial(numFlips):
    numHeads=0
    for n in range(numFlips):
        if random.random()<.5:
            numHeads+=1
    numTails=numFlips-numHeads
    return numHeads,numTails
    
def flipPlot(minExp,maxExp,numTrials):
    meanRatios,meanDiffs,ratiosSDs,diffsSDs=[],[],[],[]
    xAxis=[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios=[]
        diffs=[]
        for t in range(numTrials):
            numHeads,numTails=runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads-numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    pylab.plot(xAxis,meanRatios,'bo')
    pylab.title('Mean Heads/Tails Ratios('+str(numTrials)+' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.figure()
    pylab.plot(xAxis,ratiosSDs,'bo')
    pylab.title('SD Heads/Tails Ratios ('+str(numTrials)+' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title('Mean abs(#Heads-#Tails) ('+str(numTrials)+' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean abs(#Heads-#Tails)')
    pylab.plot(xAxis,meanDiffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis,diffsSDs,'bo')
    pylab.title('SD abs(#Heads-#Tails) ('+str(numTrials)+' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    
#flipPlot(4,20,20)
#pylab.show()

def CV(x):
    '''Coefficient of variation: Coefficient of Variation should only be
    computed on ratio scales (i.e., data where there is a "true" zero, 
    like temperatures in Kelvin, or heights, or sizes of populations, etc). 
    Coefficient of Variation may not be meaningful for data that does not 
    have a "true" zero. Temps in C, for instance would be invalid, because 
    negative values, as well as datasets where the mean could be 0.'''
    mean=sum(x)/float(len(x))
    try:
        return stdDev(x)/mean
    except ZeroDivisionError:
        return float('NaN')

