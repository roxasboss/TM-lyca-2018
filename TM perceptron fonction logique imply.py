# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:29:05 2018

@author: Maxwell
"""

import numpy as np

def Heavside_function(x): #activation, la fonction de Heavside fonctionne bien ici car on veut un résultat de 0 ou 1
    if x >=0:
        return 1
    else:
        return 0
inputs =np.array([[0,0],[0,1],[1,0],[1,1]])    
outputs = np.array([[1],[1],[0],[1]])
w1 = 0.1 #2 poids synaptique car 2 input à chaque fois 
w2 = 1
b = 0
learning_rate = 0.9
for i in range (10):
    for j in range (4): #on iter i fois à travers chaque ligne(4 ici)
        z= inputs[j][0]*w1 + inputs[j][1]*w2 + b 
        prediction = Heavside_function(z)
        cost = outputs[j]-prediction
        w1 = w1 +learning_rate*(cost)*inputs[j][0]
        w2 = w2 +learning_rate*(cost)*inputs[j][1]
        b =  b+learning_rate*(cost)
print (cost)
z1 = str(Heavside_function(w1*0 + w2 *0+ b))
z2 = str(Heavside_function(w1*0 + w2 *1+ b))
z3 = str(Heavside_function(w1*1 + w2 *0+ b))
z4 = str(Heavside_function(w1*1 + w2 *1+ b))
print ("0 & 0: " +z1)
print ("0 & 1: " +z2)
print ("1 & 0: " +z3)
print ("1 & 1: " +z4)