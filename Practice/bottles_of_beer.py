# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:35:43 2015

@author: swoop
"""

bottles_of_beer_on_the_wall = 99

while bottles_of_beer_on_the_wall > 0:
    if bottles_of_beer_on_the_wall >= 2:
        print str(bottles_of_beer_on_the_wall) + " bottles of beer on the wall, " + str(bottles_of_beer_on_the_wall) + " bottles of beer. Take one down, pass it around, "
        bottles_of_beer_on_the_wall -= 1
        if bottles_of_beer_on_the_wall == 1:
            print str(bottles_of_beer_on_the_wall) + " bottle of beer on the wall!"
        else:
            print str(bottles_of_beer_on_the_wall) + " bottles of beer on the wall!"
    else:
        print str(bottles_of_beer_on_the_wall) + " bottle of beer on the wall " + str(bottles_of_beer_on_the_wall) + " bottle of beer. Take it down, pass it around, and there's no more bottles of beer on the wall!"
        bottles_of_beer_on_the_wall -= 1
        