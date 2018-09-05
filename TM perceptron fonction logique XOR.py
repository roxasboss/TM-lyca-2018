# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:29:05 2018

@author: Maxwell
"""

import numpy as np

"""activation, la fonction de Heavside(threshold) fonctionne bien ici 
car on veut un résultat de 0 ou 1"""
def threshold(x): 
    if x >=0:
        return 1
    else:
        return 0
inputs =np.array([[0,0],[0,1],[1,0],[1,1]])    
outputs = np.array([[0],[1],[1],[1]])
w1 = 0.1 #2 poids synaptique car 2 input à chaque fois 
w2 = 1
b = 1
learning_rate = 0.25
for i in range (10):
    for j in range (4): #on iter i fois à travers chaque ligne(4 ici)
        z= inputs[j][0]*w1 + inputs[j][1]*w2 + b 
        prediction = threshold(z)
        cost = outputs[j]-prediction
        w1 = w1 +learning_rate*(cost)*inputs[j][0]
        w2 = w2 +learning_rate*(cost)*inputs[j][1]
        b =  b+learning_rate*(cost)
print ("OR: ")
print (cost)
z1 = (threshold(w1*0 + w2 *0+ b))
z2 =(threshold(w1*0 + w2 *1+ b))
z3 = (threshold(w1*1 + w2 *0+ b))
z4 = (threshold(w1*1 + w2 *1+ b))
print ("0 0: " +str(z1))
print ("0 1: " +str(z2))
print ("1 0: " +str(z3))
print ("1 1: " +str(z4))
print(str(w1),str(w2),str(b))
inputs =np.array([[0,0],[0,1],[1,0],[1,1]])    
outputs = np.array([[0],[0],[0],[1]])
w1p = 0.1 #2 poids synaptique car 2 input à chaque fois 
w2p = 1
bp = 1

for i in range (10):
    for j in range (4): #on iter i fois à travers chaque ligne(4 ici)
        z= inputs[j][0]*w1p + inputs[j][1]*w2p + bp
        prediction = threshold(z)
        cost = outputs[j]-prediction
        w1p = w1p +learning_rate*(cost)*inputs[j][0]
        w2p = w2p +learning_rate*(cost)*inputs[j][1]
        bp =  bp+learning_rate*(cost)
print("AND: ")
print (cost)
z1p = (threshold(w1p*0 + w2p *0+ bp))
z2p = (threshold(w1p*0 + w2p *1+ bp))
z3p = (threshold(w1p*1 + w2p *0+ bp))
z4p = (threshold(w1p*1 + w2p *1+ bp))
print ("0 0: " +str(z1p))
print ("0 1: " +str(z2p))
print ("1 0: " +str(z3p))
print ("1 1: " +str(z4p))



def ander(x,y):
    return threshold(w1p*x+w2p*y+bp)

def orer(x,y):
       return threshold(w1*x+w2*y+b)

"""On change l'input pour le rendre la fonction linéairement séparable: on remplace 
x1 par AND(x1,x2) et x2 par OR (x1,x2)"""
inputs =np.array([[(z1p),(z1)],[(z2p),(z2)],[(z3p),(z3)],[(z4p),(z4)]])    
outputs = np.array([[0],[1],[1],[0]])
w1s = 0.1 #2 poids synaptique car 2 input à chaque fois 
w2s = 1
bs = 1

for i in range (10):
    for j in range (4): #on iter i fois à travers chaque ligne(4 ici)
        zpp= inputs[j][0]*w1s + inputs[j][1]*w2s + bs 
        prediction = threshold(zpp)
        cost = outputs[j]-prediction
        w1s += learning_rate*(cost)*inputs[j][0]
        w2s += learning_rate*(cost)*inputs[j][1]
        bs +=  learning_rate*(cost)
print ("XOR: ")
print (cost)
z1pp = (threshold(w1s*ander(0,0) + w2s *orer(0,0)+ bs))
z2pp = (threshold(w1s*ander(0,1) + w2s *orer(0,1)+ bs))
z3pp = (threshold(w1s*ander(1,0) + w2s *orer(1,0)+ bs))
z4pp =(threshold(w1s*ander(1,1) + w2s *orer(1,1)+ bs))
print ("AND(0,0) OR(0,0): " +str(z1pp))
print ("AND(0,1) OR(0,1): " +str(z2pp))
print ("AND(1,0) OR(1,0): " +str(z3pp))
print ("AND(1,1) OR(1,1): " +str(z4pp))

