# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:47:37 2014

@author: swoop
"""
import math
import operator
import numpy as np
import matplotlib.pylab as plt

'''This program currently simulates the work of a FrontLoader moving material
in a RockQuarry. Additional machinery is planned. To test it with basic parameters, 
run the code, and then call 'go()' at the terminal prompt.'''

class RockQuarry(object):
    '''
    Creates a numpy array representing a single quarry site with material to be processed.
    
    The quarry is a defined 2d-area, and uniform randomly generated floats
    represent material density.
    '''
    def __init__(self,width=4,height=4,matLow=2.5,matHigh=10):
        """
        Initializes a rectangular quarry with the specified width and height.
        Defaults represent 1 square meter grid, for a quarry patio 100m x 100m in area.

        Initially, each 'tile' in 'grid' has a uniformly selected random float
        from matLow to matHigh representing the amount of material at that location.

        width: an integer > 0
        height: an integer > 0
        cleared: number of tiles completley cleared of material
        """
        self.width=width
        self.height=height
        self.matLow=matLow
        self.grid=np.random.uniform(matLow,matHigh,(height,width))
        self.origin=Position(self.height-1,self.width-1)
        self.grid[height-1,width-1]=0.0
        self.Stockpile=self.grid[height-1,width-1]  
        self.cleared=0
        
    def loadAtPosition(self,pos,loadCap):
        """
        Remove material equal to the loader capacity from position.

        Assumes that POS represents a valid position inside this room,

        pos: a Position
        """   
        if self.grid[pos.x,pos.y]>0:
            self.grid[pos.x,pos.y]-=loadCap
    
    def getGridArea(self):
        """
        Return the total number of tiles in the quarry.

        returns: an integer
        """
        return str(self.width*self.height)

    def getStockpile(self):
        """
        Return the total amount in the Stockpile.

        returns: an integer
        """
        return self.Stockpile
        
    def getOrigin(self):
        """
        Returns the origin inside the quarry. This is used by FrontLoader as it's
        material delivery location. Default is the bottom right of the quarry.

        returns: a Position object.
        """
        return self.origin
    
    def getDistToOrigin(self,pos):
        '''pythagoras!'''
        a=self.width-pos.x
        b=self.height-pos.y
        c=a**2+b**2 #may have to be abs()...
        return math.sqrt(c)
        
    def isInQuarry(self,m,n):
        """
        Return True if (m,n) is inside the quarry.

        m: an integer
        n: an integer
        returns: True if pos is in the quarry, False otherwise.
        """
        if m>=0.0 and n>=0.0:
            try:
                self.grid[m,n]
                return True
            except IndexError:
                return False
        else:
            return False  
    
    def matAtTile(self,m,n):
        """
        Return True if the tile (m, n) has been cleared.

        Assumes that (m, n) represents a valid tile inside the quarry.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleared, amount of remaining material otherwise.
        """
        if self.grid[m,n]>0.0:
            return self.grid[m,n]
        else:
            return True        
            
    def surveyPosition(self,currentPos):
        """
        Build a list of adjacent squares and their material amounts.
        
        If there is no material at the current location, return the adjecent
        position with material that is closest to the origin.

        returns: a Position object.
        """
        coords={'-1,-1':0.0,'-1,0':0.0,'-1,1':0.0,'0,-1':0.0,'0,0':0.0,\
        '0,1':0.0,'1,-1':0.0,'1,0':0.0,'1,1':0.0}
        if self.matAtTile(currentPos.x,currentPos.y)<=self.matLow:
            print '\n'+'There is not enough Material in this area.'+'\n'+'Surveying...','\n',\
            self.grid
            self.cleared+=1
            for i in range(-1,2):
                for j in range(-1,2):
                    if currentPos.x+i < self.width and currentPos.y+i < self.height\
                    and currentPos.x+j < self.width and currentPos.y+j < self.height:
                        if self.matAtTile(currentPos.x+i,currentPos.y+j)>0.0 and \
                        self.isInQuarry(currentPos.x+i,currentPos.y+j):#make sure there's material at the candidate...make sure it's in the quarry...
                            coords[str(i)+','+str(j)]=self.getDistToOrigin(Position(currentPos.x+i,currentPos.y+j))#find distances of candidates
    
            nextCandidate=max(coords.iteritems(), key=operator.itemgetter(1))[0].split(",")
            nextTile=Position(currentPos.getX()+int(nextCandidate[0]),currentPos.getY()+int(nextCandidate[1]))
            print 'Found a new spot, boss.','\n','- Coordinates are:',nextTile   
            return nextTile
        else:
            return currentPos
            
class FrontLoader(object):    
    '''
    Represents a single frontloader moving rocks.

    At all times the frontloader has a phase (toMat, loading, toStock, dumping)
    in the quarry.
    The frontloader also has a fixed speed, a load capacity, and it tracks its
    bucket fill status and the amount of work that it has done.

    Subclasses of FrontLoader should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    '''
    def __init__(self, quarry, speed=5, loadCap=2.5):
        '''
        Initializes a FrontLoader with the given speed in the specified quarry. The
        robot starts in the 'toMat' phase, at the 'origin', to which it will return.
        The robot cleans the tile it is on.

        quarry= a RockQuarry object.
        speed: a float (speed > 0)
        '''
        self.quarry=quarry
        self.pos=self.quarry.getOrigin()
        self.phase='toMat'
        self.speed=float(speed)#in KPH
        self.loadCap=loadCap
        self.loadStatus='- Bucket Status: Empty.'
        self.workDone=[]
        self.workDoneRatio=[]
        self.tolva=[]

    def getLoaderPosition(self):
        '''
        Return the position of the frontloader.

        returns: a Position object giving the frontloader's position.
        '''
        return self.pos
            
    def getLoaderPhase(self):
        """
        Return the phase of the loader: toMat, loading, toStock, dumping. 

        returns: a string giving the phase of the loader in process of extraction.
        """
        return self.phase

    def setLoaderPosition(self, position):
        """
        Set the position of the loader to 'position'.

        position: a Position object.
        """
        if self.quarry.isPositionInQuarry(position):
            self.pos=position

    def setLoaderPhase(self, phase):
        """
        Set the phase of the loader to 'phase'.

        phase: a string representing the phase of the loader in process of extraction.
        """
        self.phase=phase
    
    def matAtPos(self,pos):
        """
        Return True if the tile (m, n) has been cleared.

        Assumes that (m, n) represents a valid tile inside the quarry.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleared, amount of remaining material otherwise.
        """
        if self.quarry.grid[pos.x,pos.y]<=self.loadCap:
            return self.quarry.grid[pos.x,pos.y]
        else:
            return self.quarry.grid[pos.x,pos.y]

    def updatePositionAndPhase(self):
        """
        Simulate work. 
        """
        if self.phase=='toMat':
            self.pos=self.quarry.surveyPosition(self.pos)#find the closest tile with material, and favor the more material       
            toOrig=self.quarry.getDistToOrigin(self.pos)
            tTime=toOrig/self.speed
            self.workDone.append(tTime)
            if len(self.tolva)<1:
                self.tolva.append(0.0)
            else:
                self.tolva.append(self.tolva[-1])
            self.phase='loading'
            print 'Going to work.'+'\n'+'- Transit Time to site:',round(float(tTime),2),\
            'units.'+'\n'+'- Material Density:',round(float(self.matAtPos(self.pos)),2),\
            'm3.'+'\n',self.loadStatus,'\n'+'Heading to the site.'
            
        elif self.phase=='loading':
            self.quarry.loadAtPosition(self.pos,self.loadCap)
            self.phase='toStock'         
            self.loadStatus='- Bucket Status: Full Load'
            print 'Arrived at site and Loaded-up.'+'\n','-',round(float(self.matAtPos(self.pos)),2),\
            'm3 of remaining Material.','\n',self.loadStatus,'('+str(self.loadCap),\
            'm3 of material).'+'\n'+'Ready to move out.'
                                
        elif self.phase=='toStock':
            toOrig=self.quarry.getDistToOrigin(self.pos)
            tTime=toOrig/self.speed #dist=r*t...
            self.workDone.append(tTime)
            self.phase='dumping'
            print 'Heading back to Stockpile.','\n','- Transit Time to Stockpile:',\
            round(tTime,2),'units.','\n',self.loadStatus,'('+str(self.loadCap),'m3 of material).'
            
        elif self.phase=='dumping':
            if self.matAtPos(self.pos)<self.loadCap:
                self.pos=self.quarry.getOrigin()
            self.quarry.Stockpile+=self.loadCap
            self.tolva.append(self.quarry.Stockpile)
            self.phase='toMat'
            self.loadStatus='Bucket Status: Empty Load'
            self.workDoneRatio.append(round(float(self.quarry.Stockpile/sum(self.workDone)),4))
            print 'Setting her down, boss.'+'\n'+'- Material in Stockpile:',\
            round(float(self.quarry.Stockpile),2),'\n','- Units Worked:',round(float(sum(self.workDone)),2),\
            '\n','- Stock/Time Ratio:',round(float(self.quarry.Stockpile/sum(self.workDone)),4),\
            '\n','- Quarry Area Cleared:',self.quarry.cleared,'of',self.quarry.getGridArea(),'tiles.',

#class tolva():
#    def __init__(self, quarry, speed=5, loadCap=2.5):
#        '''
#        Initializes a FrontLoader with the given speed in the specified quarry. The
#        robot starts in the 'toMat' phase, at the 'origin', to which it will return.
#        The robot cleans the tile it is on.
#
#        quarry= a RockQuarry object.
#        speed: a float (speed > 0)
#        '''
#        self.quarry=quarry
#        self.origin=self.quarry.getOrigin()
#        self.pos=self.origin
#        self.phase='toMat'
#        self.speed=float(speed)#in KPH
#        self.loadCap=loadCap
#        self.loadStatus='Bucket Status: Empty.'
#        self.workDone=0.0
#        self.workDoneRatio=[]
#        self.tolva=[]
     
class Position(object):
    """
    A Position represents a location in a two-dimensional quarry.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

PA=FrontLoader(RockQuarry())

def go(loader):
    loader.updatePositionAndPhase()


def goPlot(loader):
    for i in xrange(100):
        loader.updatePositionAndPhase()
    plt.figure(1)
    plt.plot(loader.workDoneRatio)
    plt.title('Work/Time Ratio Over Time')
    plt.xlabel('Time')
    plt.ylabel('Time/Work Ratio')
    plt.figure(2)
    plt.plot(loader.workDone,loader.tolva)
    plt.title('Time for Material')
    plt.xlabel('Time Per Trip')
    plt.ylabel('Tolva Material Level')
    plt.show()
    
#goPlot(PA)
go(PA)
