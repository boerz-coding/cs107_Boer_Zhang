#Coder: Matthew Stewart
#Sharer: Apisada (Ju) Chulakadabba
#Listener: Boer Zhang

import numpy as np

class Layer():
#    """Implements a neural network layer."""
    
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.rand(self.shape[0],self.shape[1])/100
        self.bias = np.random.rand(self.shape[1])/100

    def forward(self, inputs, value=0.1):
        return self.actv(np.dot(inputs,self.weights)+self.bias)

    def __str__(self):
        return f"This is a {type(self).__name__} class."

    def __repr__(self):
        return f"{type(self).__name__}({self.shape},{self.actv})."

    def __len__(self):
        return self.shape[0]


t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

shape1 = [100,100]
shape2 = [100,1]

# Run through the network
layer1 = Layer(shape1, np.tanh) # First layer
layer2 = Layer(shape2, np.tanh) # Last layer

h1 = layer1.forward(t)
h2 = layer2.forward(h1)
