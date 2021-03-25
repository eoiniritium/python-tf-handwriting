import numpy as np
from random import uniform
import random

def rnd(start, stop):
    return random.uniform(start, stop)

def printmodel(model):
    for layer in model:
        for node in layer:
            print(str(node[0]) + " ")
            for k in range(1, len(node)):
                print(str(node[k]) + ", ")
            print("\n") #Next node
        print("\n\n") #Next node layer

def generatemodel(indim, hilay, hilaydim, outdim, rmin, rmax): #input dimension, number of hidden layers, hidden layer dimension, output layer dimension, random minimum, random maximum
    top = []
    layer = []
    node = []
    
    #First layer
    for i in range(indim + 1):
        node.clear()
        node.append(1) #Bias placeholder
        for x in range(hilaydim):
            node.append(rnd(rmin, rmax))
        layer.append(node)
    top.append(top)
    layer.clear()

    #Hidden layers
    for i in range(hilay - 1):
        layer.clear()
        for j in range(hilaydim): #For every node
            node.clear()
            node.append(1) #Bias placeholder
            for k in range(hilaydim): #For everynode in the next layer
                node.append(rnd(rmin, rmax))
            layer.append(node)
        top.append(layer)
    
    #Last hidden layer (exception to the rule because it has a number of connections of the ouput layer not the next hidden layer)
    for i in range(hilaydim):
        node.clear()
        node.append(1)
        for k in range(outdim):
            node.append(rnd(rmin, rmax))
        layer.append(node)
    top.append(layer)
    layer.clear()

    #Output layer
    for i in range(outdim):
        node.clear()
        node.append(0)
        layer.append(node)
    top.append(layer)
    layer.clear()
    return top

printmodel(generatemodel(3, 2, 3, 2, 0.5, 1.5))
print(rnd(0.0, 0.6))