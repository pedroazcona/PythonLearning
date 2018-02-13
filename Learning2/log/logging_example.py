# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:25:13 2018

@author: poaa
"""

import logging

logging.basicConfig(filename=r'C:\Users\poaa\Documents\Python Scripts\Learning2\log\example.log',filemode='w', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
