# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:06:36 2018

@author: Maxwell"""
import numpy as np

def Heavside_function(x): #activation, la fonction de Heavside fonctionne bien ici car on veut un résultat de 0 ou 1
    if x >=0:
        return 1
    else:
        return 0
def sigmoid(x):
    return 1./(1.+np.exp(-x))

def transfer(x):
    return sigmoid(x)
#   return Heavside_function(x)

inputs =np.array([[0,0],[0,1],[1,0],[1,1]])    
outputs = np.array([[0],[0],[0],[1]])
w1 = np.random.rand() #2 poids synaptique car 2 input à chaque fois 
w2 = np.random.rand()
b = np.random.rand()
learning_rate = 0.5
maxiter=1000
for i in range (maxiter):
    tot_cost=0
    for j in range (4): #on iter i fois à travers chaque ligne(4 ici)
        z= inputs[j][0]*w1 + inputs[j][1]*w2 + b 
        prediction = transfer(z)
        cost = outputs[j]-prediction
        tot_cost += abs(cost)
        w1 += learning_rate*(cost)*inputs[j][0]
        w2 += learning_rate*(cost)*inputs[j][1]
        b += learning_rate*(cost)
    if tot_cost <=1e-3:
        print("current iteration:"+str(i))
        break
print (cost,)
z1 = str(transfer(w1*0 + w2 *0+ b))
z2 = str(transfer(w1*0 + w2 *1+ b))
z3 = str(transfer(w1*1 + w2 *0+ b))
z4 = str(transfer(w1*1 + w2 *1+ b))
print ("0 & 0: " +z1)
print ("0 & 1: " +z2)
print ("1 & 0: " +z3)
print ("1 & 1: " +z4)
            
            