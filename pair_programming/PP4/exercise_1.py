# Coder: Boer Zhang
# Sharer: Kevin Hare
# Listener: Mark Penrod


import numpy as np
##closure part
def layer(shape, actv):
    def inner(inputs, weights, bias):
        hout=actv(np.dot(weights,inputs.T)+bias)
        return hout
    return inner

##Some input
t = np.random.uniform(0.0, 1.0, 4).reshape(1,-1) # 100x1 vertical vector
shape1=list([4,4])
shape2=list([4,2])
layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.ones([4,4])#
w2 = np.ones([2,4])#
b1 = 0.00001*np.random.uniform(0.0, 1.0, 4).reshape(1,-1) # 100x1 vertical vector
b2 = 0.00001*np.random.uniform(0.0, 1.0, 4).reshape(1,-1) # 100x1 vertical vector

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layerde here.
print("t:",t)
print("h1:",h1)
print("h2:",h2)
