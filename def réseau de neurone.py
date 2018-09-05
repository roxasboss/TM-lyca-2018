# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:10:07 2018

@author: Maxwell
"""

def Logistic(x):
    return 1/(1+np.exp(-x))
def backpropagation(x,yt,L,wij):
    for i in range(wij):
        weights=np.array([[]])