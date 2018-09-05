# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:49:28 2018

@author: Maxwell
"""

import numpy as np
inputs =np.array([[0,0],[0,1],[1,0],[1,1]])    
outputs = np.array([[0],[1],[1],[0]])

b3=1
b4=1
b5=1
b6=1
b7=1



w13=0.1
w14=0.1
w23=0.1
w24=0.1
w35=0.1
w45=0.1

alpha =0.4
def sigmoid(x):
    return 1/(1+np.exp(-x))
"def backpropagation:"
    
for i in range (10000):
    for j in range(4):
        a3=sigmoid(inputs[j][0]*w13+inputs[j][1]*w23+b3)#premier neurone
        a4=sigmoid(inputs[j][0]*w14+inputs[j][1]*w24+b4)#2ème neurone
        a5=sigmoid(a3*w35+a4*w45+b5)#3ème neurone 
       
        costa5= outputs[j]-a5
        costa4 = a4*(1-a4)*w45*costa5
        costa3 = a3*(1-a3)*w35*costa5
        b3= b3+alpha*costa3
        b4=b4+alpha*costa4
        b5=b5+alpha*costa5

        w13 =w13 +alpha*inputs[j][0]*costa3
        w14 =w14 +alpha*inputs[j][0]*costa4
        w23 =w23 +alpha*inputs[j][1]*costa3
        w24 =w24 +alpha*inputs[j][1]*costa4
        w35 =w35 +alpha*a3*costa5

print(costa5)
print(costa3)
print(costa4)     
print ("erreur: " + str(costa5))
a3=sigmoid(0*w13+0*w23+b3)#premier neurone
a4=sigmoid(0*w14+0*w24+b4)#2ème neurone
a5=sigmoid(a3*w35+a4*w45+b5)#3ème neurone 
print (a5)

a3=sigmoid(0*w13+1*w23+b3)#premier neurone
a4=sigmoid(0*w14+1*w24+b4)#2ème neurone
a5=sigmoid(a3*w35+a4*w45+b5)#3ème neurone 
print (a5)

a3=sigmoid(1*w13+0*w23+b3)#premier neurone
a4=sigmoid(1*w14+0*w24+b4)#2ème neurone
a5=sigmoid(a3*w35+a4*w45+b5)#3ème neurone 
print (a5)

a3=sigmoid(1*w13+1*w23+b3)#premier neurone
a4=sigmoid(1*w14+1*w24+b4)#2ème neurone
a5=sigmoid(a3*w35+a4*w45+b5)#3ème neurone 
print (a5)