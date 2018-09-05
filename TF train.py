# -*- coding: utf-8 -*-






import numpy as np  
import pandas as pd  
import urllib.request as request  
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
dtype = torch.DoubleTensor
N, D_in, H, D_out = 120, 4, 5, 3
IRIS_TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

names = ['sepal-length', 'sepal-width', 
         'petal-length', 'petal-width', 'species'] 
train = pd.read_csv(IRIS_TRAIN_URL, names=names, skiprows=1)
test = pd.read_csv(IRIS_TEST_URL, names=names, skiprows=1)
Xtrain = train.drop("species",axis=1)
Xtest = test.drop("species", axis=1)

Xtrain = Xtrain.values
Xtrain = torch.from_numpy(Xtrain)

ytrain = pd.get_dummies(train.species)

ytrain = ytrain.values
ytrain = torch.from_numpy(ytrain)

ytest = pd.get_dummies(test.species)


x = Variable(Xtrain,requires_grad=False)
y = Variable(ytrain, requires_grad= False)

wl1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
wl2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)

learning_rate = 0.05
for i in range(500):
    y_pred = x.mm(wl1).clamp(min=0).mm(wl2)
    loss = (y_pred-y).pow(2).sum() #MSE
    print(i, loss.data[0])
    
    loss.backward()
    
    wl1.data -= learning_rate*wl1.grad.data
    wl2.data -= learning_rate*wl2.grad.data
    
    wl1.grad.data.zero_()
    wl2.grad.data.zero_()
    

"""import tensorflow as tf

tf.reset_default_graph()

# Define a placeholder
a = tf.placeholder("float", name='pholdA')  
print("a:", a)

# Define a variable 
b = tf.Variable(2.0, name='varB')  
print("b:", b)

# Define a constant
c = tf.constant([1., 2., 3., 4.], name='consC')  
print("c:", c)"""      

    
    
    

    
    