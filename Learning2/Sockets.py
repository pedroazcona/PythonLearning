# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:59:58 2018

@author: poaa
"""
import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
