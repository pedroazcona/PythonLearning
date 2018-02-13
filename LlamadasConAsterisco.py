# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:44:04 2018

@author: poaa
"""

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print("-" * 40)
    print("-" * 40)
    print (keywords)


cheeseshop("Limburger", #kind
           "It's very runny, sir.", # *arguments[0]
           "It's really very, VERY runny, sir.",# *arguments[1]
           shopkeeper="Michael Palin", #**keywords[0]
           client="John Cleese", #**keywords[1]
           sketch="Cheese Shop Sketch",
           mamporrero="Pablo Iglesias",) #**keywords[3]


def f (x): return x**2