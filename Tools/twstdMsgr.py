# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
A very simple Twisted Jabber client

To run the script:

    $ python jabber_client.py
"""

# Originally written by Darryl Vandorp
# http://randomthoughts.vandorp.ca/

from twisted.words.protocols.jabber import client, jid
from twisted.words.xish import domish
from twisted.internet import reactor
        
def authd(xmlstream):
    print "authenticated"

    presence = domish.Element(('jabber:client','presence'))
    xmlstream.send(presence)
    
    xmlstream.addObserver('/message',  debug)
    xmlstream.addObserver('/presence', debug)
    xmlstream.addObserver('/iq',       debug)   

def authfailedEvent(xmlstream):
	global reactor
	print 'Auth failed!'
	reactor.stop()

def debug(elem):
    print elem.toXml().encode('utf-8')
    print "="*20
    
myJid = jid.JID('pynanc3@gmail.com')
factory = client.basicClientFactory(myJid, 'quant6512')
factory.addBootstrap('//event/stream/authd',authd)
factory.addBootstrap('//event/stream/authfailedEvent',authfailedEvent)
reactor.connectTCP('talk.google.com',5222,factory)
reactor.run()
