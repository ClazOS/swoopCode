# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 11:30:23 2014

@author: swoop
"""

# Import smtplib for the actual sending function
import smtplib

fromaddr = 'pynanc3@gmail.com'
toaddrs  = 'cclasby@gmail.com'
msg = "\r\n".join([
  "From: "+fromaddr,
  "To: "+toaddrs,
  "Subject: Well, it works.",
  "",
  "Hey now."
  ])
username = 'pynanc3@gmail.com'
password = 'f7ddupCJ1'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()