import numpy as np
from algorithm import neuralnetwork as nn

weights = np.array([0.5, 0.1]).reshape(1,2) # initial weights
learning_rate = 0.001
bias = -0.1
perceptron = nn.NeuralNetwork(weights, learning_rate, bias)
perceptron.execute()