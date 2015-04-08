# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 23:33:35 2014

@author: swoop
"""

#import twitter
import requests
from lxml import html
import random
import time

'''

''' 
#
#def tweetHeadline(msg,accessToken='2193344742-iKr46uz1hRPvlmcC38JiTU0qRlJtJf5p2NylN2L',\
#                        tokenSec='zAocuHCcugEIwvtp4IQX0f1RsplbrhR3ERbS7BqEUVwEq',\
#                        cosKey='IkgKVEyGGQUzfjjZFAvMbodxF',\
#                        conSec='HdzrI7MVKTKfRcqeK5dpsmn0BiBfKZbJ8QjqFCMspiGYc9vFG3'):
#    my_auth = twitter.OAuth(accessToken,tokenSec,cosKey,conSec)
#    twit = twitter.Twitter(auth=my_auth) 
#    if msg != None:
#        print msg
#        twit.statuses.update(status=msg)
#    else:
#        print 'Nuthin fo ya bahws.'
        
def scoreFetcher(): #returns a dict of 'fixtures'
        page=requests.get('http://finance.yahoo.com/')
        tree=html.fromstring(page.text)
#        headline=tree.xpath('//*[@id="yui_3_16_0_1_1415208010122_858"]/text()')
        print tree

scoreFetcher()
        
