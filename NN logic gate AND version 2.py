#
import numpy as np
#input and target output
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
outputs = np.array([[0],[0],[0],[1]])
#structure
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()
# activation
a=1
epsilon=1e-5

def sigmoid(x):
    return 1/(1+np.exp(-a*x))
def sigmoid_p(x): #derivative of the sigmoid function
    return a*sigmoid(x) * (1-sigmoid(x))
#training loop
learning_rate = 2 #coefficient
for i in range(100000):
#    random_index = np.random.randint(len(data))#set a random index =length data -1
#    point = data[random_index] #take a random row of the matrix
    delta=0
    for j in range(4):
        z =inputs[j][0]*w1 + inputs[j][1]*w2 +b
        h = sigmoid(z) #prediction
        target = outputs[j] # point[2]
        cost = np.square(h - target) #cost fucntion
        
        #chain rule with linear regression:
        dcost_dpred = 2*(h-target) #derivative of the cost function
        dpred_dz = sigmoid_p(z) #derivative of the sigmoid of z

        dz_dw1 = inputs[j][0]
        dz_dw2 = inputs[j][1]
        dz_db = 1

        dcost_dz = dcost_dpred * dpred_dz
        dcost_dw1 = dcost_dz * dz_dw1 #slope of the cost function on w1
        dcost_dw2 = dcost_dz * dz_dw2 #slope of the cost function on w2
        dcost_db = dcost_dz * dz_db #slope of the cost function on b
        #update weights and bias
        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db
        delta += abs(cost)
    delta=0.
    print(delta)
    if delta<epsilon: break
    
print (cost,i)
y = w1 *np.array([0,0,1, 1])+ w2 * np.array([0,1,0,1])+ np.array([b,b,b,b])
pred = sigmoid(y)
print(pred)
z1 = str(sigmoid(w1*0 + w2 *0+ b))
z2 = str(sigmoid(w1*0 + w2 *1+ b))
z3 = str(sigmoid(w1*1 + w2 *0+ b))
z4 = str(sigmoid(w1*1 + w2 *1+ b))
print ("0 & 0: " +z1)
print ("0 & 1: " +z2)
print ("1 & 0: " +z3)
print ("1 & 1: " +z4)



