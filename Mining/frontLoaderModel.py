# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 20:47:37 2014

@author: swoop
"""
import numpy as np
import matplotlib.pyplot as plt

class RockQuarry(object):
    '''
    Represents a single quarry site with material in a particular ratio.
    
    The quarry as a defined area, and uniform material density in the defined ratio.
    '''
    def __init__(self, width=100, height=100, matLow=2.5, matHigh=100):
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
        self.tiles=np.random.uniform(matLow,matHigh,(width,height))
        self.clear=0
        
    
    def loadAtPosition(self, pos, loadCap):
        """
        Remove material equal to the loader capacity at position.

        Assumes that POS represents a valid position inside this room,

        pos: a Position
        """   
        if self.tiles[pos.x,pos.y]>0:
            self.tiles[pos.x,pos.y]-=loadCap
        else:
            self.clear+=1
        #need to send this material to the front loader... loadCap?

    def isTileEmpty(self, m, n):
        """
        Return True if the tile (m, n) has been cleared.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.tiles[m,n]==1:
            return True
        else:
            return False
    
    def getNumMatTiles(self):
        """
        Return the total number of tiles in the quarry.

        returns: an integer
        """
        return self.width*self.height,

    def getNumCleanedTiles(self):
        """
        Return the total number of clear tiles in the quarry.

        returns: an integer
        """
        return self.clear

#    def getRandomPosition(self):
#        """
#        Return a random position inside the room.
#
#        returns: a Position object.
#        """
#        ans=Position(random.random()*self.width,random.random()*self.height)
#        return ans

    def isPositionQuarry(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.x>=0.0 and pos.y>=0.0:
            try:
                self.tiles[pos.x,pos.y]
                return True
            except IndexError:
                return False
        else:
            return False
        

#class frontLoader(object):    
     """
    Represents a single frontloader moving rocks.

    At all times the front loader has a particular position (scooping, toStock, fromStock, dumping)
    the quarry.
    The frontloader also has a fixed speed, and a load capacity.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
#    def __init__(self, room, speed):

 """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of frontLoader should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.roomquarry=room
        self.pos=self.room.getRandomPosition()
        self.direction=random.randint(0,360)
        self.speed=float(speed)
        self.room.cleanTileAtPosition(self.pos)
        

    def getLoaderPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getLoaderPhase(self):
        """
        Return the phase of the loader: 

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        if self.room.isPositionInRoom(position):
            self.pos=position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction=direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
        


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

    
priceList()
    

     