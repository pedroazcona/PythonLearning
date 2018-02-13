# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:27:22 2018

@author: poaa
"""

import webbrowser
import urllib as ur
#webbrowser.open("http://www.elmundo.es")
#webbrowser.open_new_tab("http://www.elmundo.es")
url = ur.request.urlopen("http://www.gft.com")
print(url.geturl())
print(url.info()) 