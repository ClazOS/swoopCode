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
    def __init__(self,width=100,height=100,matLow=2.5,matHigh=10):
        """
        Initializes a rectangular quarry with the specified width and height.
        Defaults represent 1 square meter tiles, for a quarry patio 100m x 100m in area.

        Initially, each 'tile' in 'tiles' has a uniformly selected random float
        from matLow to matHigh representing the amount of material at that location.

        width: an integer > 0
        height: an integer > 0
        clear: number of tiles completley cleared of material
        """
        self.width=width
        self.height=height
        self.matLow=matLow
        self.tiles=np.random.uniform(matLow,matHigh,(height,width))
        self.tiles[height-1,width-1]=0.0
        self.stockpile=self.tiles[height-1,width-1]  
        self.clear=0
        
    def loadAtPosition(self,pos,loadCap):
        """
        Remove material equal to the loader capacity from position.

        Assumes that POS represents a valid position inside this room,

        pos: a Position
        """   
        if self.tiles[pos.x,pos.y]>0:
            self.tiles[pos.x,pos.y]-=loadCap
        #need to send this material to the front loader... loadCap?
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the quarry.

        returns: an integer
        """
        return self.width*self.height,

    def getNumClearTiles(self):
        """
        Return the total number of clear tiles in the quarry.

        returns: an integer
        """
        return self.clear
        
    def getOrigin(self):
        """
        Returns the origin inside the quarry. This is used by FrontLoader as it's
        material delivery location. Default is the bottom right of the quarry.

        returns: a Position object.
        """
        ans=Position(self.height-1,self.width-1)
        return ans
    
    def isInQuarry(self,m,n):
        """
        Return True if (m,n) is inside the quarry.

        m: an integer
        n: an integer
        returns: True if pos is in the quarry, False otherwise.
        """
        if m>=0.0 and n>=0.0:
            try:
                self.tiles[m,n]
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
        if self.tiles[m,n]>0.0:
            return self.tiles[m,n]
        else:
            return True        
            
    def surveyPosition(self,currentPos):
        """
        Build a list of adjacent squares and their material amounts.
        
        Return the adjecent position with the most material.
        
        If all else fails, get a random position.

        returns: a Position object.
        """
        coords={'-1,-1':0.0,'-1,0':0.0,'-1,1':0.0,'0,-1':0.0,'0,0':0.0,\
        '0,1':0.0,'1,-1':0.0,'1,0':0.0,'1,1':0.0}
        if self.matAtTile(currentPos.x,currentPos.y)<=self.matLow:
            print 'There is not enough Material in this area. Surveying...'
            self.clear+=1
            for i in range(-1,2):
                for j in range(-1,2):
                    if currentPos.x+i < self.width and currentPos.y+i < self.height\
                    and currentPos.x+j < self.width and currentPos.y+j < self.height:
                        if self.matAtTile(currentPos.x+i,currentPos.y+j)>0.0 and \
                        self.isInQuarry(currentPos.x+i,currentPos.y+j):
                            coords[str(i)+','+str(j)]=self.quarry.grid[currentPos.x+i,currentPos.y+j]
    
            nextCandidate=max(coords.iteritems(), key=operator.itemgetter(1))[0].split(",")
            nextTile=Position(currentPos.getX()+int(nextCandidate[0]),currentPos.getY()+int(nextCandidate[1]))
            print 'Found a new spot, boss.'            
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
        self.origin=self.quarry.getOrigin()
        self.pos=self.origin
        self.phase='toMat'
        self.speed=float(speed)#in KPH
        self.loadCap=loadCap
        self.loadStatus='Bucket Status: Empty.'
        self.workDone=0.0
        self.workDoneRatio=[]
        self.tolva=[]

    def getLoaderPosition(self):
        '''
        Return the position of the frontloader.

        returns: a Position object giving the frontloader's position.
        '''
        return self.pos
    
    def getDistToOrigin(self,pos):
        '''pythagoras!'''
        a=self.quarry.width-pos.x
        b=self.quarry.width-pos.y
        c=a**2+b**2
        return math.sqrt(c)
            
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
        if self.quarry.tiles[pos.x,pos.y]<=self.loadCap:
            return self.quarry.tiles[pos.x,pos.y]
        else:
            return self.quarry.tiles[pos.x,pos.y]

    def updatePositionAndPhase(self):
        """
        Simulate work. 
        """
        if self.phase=='toMat':
            self.pos=self.quarry.surveyPosition(self.pos)#find the closest tile with material, and favor the more material       
            toOrig=self.getDistToOrigin(self.pos)
            tTime=toOrig/self.speed
            self.workDone+=tTime
            self.phase='loading'
            print 'Heading to the site. Transit time to site is',round(float(tTime),2),\
            'units of time. Coordinates are:',self.pos,'and there is',round(float(self.matAtPos(self.pos)),2),\
            'm3 of material there.',self.loadStatus 
            
        elif self.phase=='loading':
            self.quarry.loadAtPosition(self.pos,self.loadCap)
            self.phase='toStock'            
            self.loadStatus='Bucket Status: Full Load'
            print 'Loaded up and ready to move out.',self.loadStatus,' with ',self.loadCap,' of material, and',\
            round(float(self.matAtPos(self.pos)),2),'m3 of material remaining here.'
        
        elif self.phase=='toStock':
            toOrig=self.getDistToOrigin(self.pos)
            tTime=toOrig/self.speed #dist=r*t...
            self.workDone+=tTime
            self.phase='dumping'
            print 'Heading back to stockpile. It\'s going to take me about',\
            round(tTime,2),'units of time to get back to the stockpile.',self.loadStatus+'.'
            
        elif self.phase=='dumping':
            self.quarry.stockpile+=self.loadCap
            self.tolva.append(self.quarry.stockpile)
            self.phase='toMat'
            self.loadStatus='Bucket Status: Empty Load'
            self.workDoneRatio.append(round(float(self.quarry.stockpile/self.workDone),4))
            print 'Setting her down, boss. The stockpile is at',round(float(self.quarry.stockpile),2),\
            'worth of material, and I\'ve worked',round(float(self.workDone),2),'so far, a',\
            round(float(self.quarry.stockpile/self.workDone),4),'stock/time ratio.'
        
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

fl=FrontLoader(RockQuarry())

def go(loader):
    for i in xrange(500):
        loader.updatePositionAndPhase()
    plt.figure(1)
    plt.plot(fl.workDoneRatio)
#    plt.plot(fl.tolva)
#    plt.legend('FrontLoader')
    plt.title('Work/Time Ratio Over Time')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Time/Work Ratio')
    plt.show()
    
go(fl)