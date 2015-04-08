# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:08:50 2015

@author: swoop
"""

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

py = json.load(response)