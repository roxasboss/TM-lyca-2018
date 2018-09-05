import numpy as np

# sigmoid function:
def nonlin(x):
     return 1/(1+np.exp(-x))
# input dataset,the third column is the bias which is considered here as a weight:
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
# target
y = np.array([[0, 1, 1, 1]]).T
# initialize weights randomly
weights= 2*np.random.random((3,1)) - 1

for iter in range(1000):
    l0 = X
    #prediction
    l1 = nonlin(np.dot(l0, weights))
    """update weights and bias based on the error(cost)and the slope of the sigmoid of our prediction (the derivative of the sigmoid 
     function is sigmoid(x)*(1-sigmoid(x) which is equal here to l1*(1-l1)) """
    weights += np.dot(l0.T, (y - l1) * l1 * (1 - l1))
print ("Output After Training:" )
print (l1)
