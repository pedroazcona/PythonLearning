# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:49:25 2017

@author: poaa
"""
import numpy as np
import pandas as pd
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

periods=8
index = pd.date_range('1/1/2000', periods=periods, freq='7D')
df = pd.DataFrame(np.random.randn(periods,3), index=index, columns=list('ABC'))
#baseball = read_csv(’data/baseball.csv’)
k = pd.Series(np.random.randn(periods), index=index)
df.drop_duplicates('A')

