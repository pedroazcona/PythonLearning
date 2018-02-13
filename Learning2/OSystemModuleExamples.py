# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:03:44 2018

@author: poaa
"""

import os
if os.name == 'nt':
    print('Sistema Operativo windows NT')
else:
    print('Sistema Operativo '+ os.name)
print (os.environ)
print (os.linesep)
for i in range (0,42):
    print (str(i) + ' ' + os.strerror(i))