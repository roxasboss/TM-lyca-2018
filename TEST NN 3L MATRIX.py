# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:03:01 2018

@author: Maxwell
"""

import numpy as np 

def sigmoid(x):
    return 1/(1 + np.exp(-x))
def deriv_sig(x):
    return x*(1-x)    
x = np.array([[0,0],[0,1],[1,0],[1,1]])
yt =np.array([[0],[1],[1],[0]]) 
bl0=1
bl1=1

wl0 = np.random.random((2,4)) 
wl1 = np.random.random((4,1)) 
learning_rate= 0.9
for i in range(6000):
    l1 = sigmoid(np.dot(x,wl0)+bl0)
    l2 = sigmoid(np.dot(l1,wl1)+bl1)
    error_l2 = (yt-l2)
    delta_l2 = deriv_sig(l2)*error_l2
    if (i% 1000) == 0:
        print ("Error:" + str(np.mean(np.abs(error_l2))))
    if np.mean(np.abs(error_l2)) <= 0.001:
        print("itérations: " + str(i))
        break
    
    weightx_error=np.dot(wl1.T,delta_l2)
    delta_l1 = np.dot((deriv_sig(l2)),weightx_error)
    wl1 += learning_rate*np.dot(l1.T,delta_l2)
    wl0 += learning_rate*np.dot(x.T,delta_l1)
    bl1 += learning_rate*error_l2
    bl0 += learning_rate*error_l2
print(l2)    
    
    