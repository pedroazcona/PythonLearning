# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:56:11 2017

@author: poaa
"""

import pandas as pd



Pandemia = pd.read_csv(r'C:\Users\poaa\Documents\PENTAHO_TEST\test_result.txt', sep=';')

iris=Pandemia.price
print(iris)
iris.plot()

#scatter = scatter_matrix(iris, figsize=(6,6),diagonal='kde')
#resultado = scatter.get_figure()