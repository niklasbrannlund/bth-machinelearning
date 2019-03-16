import numpy as np

P = np.array([0, 0, 0, 1, 1, 0, 1, 1]).reshape(4,2) # input 
t = np.array([0, 0, 1, 1]).reshape(4,1)
weights = np.array([0.5, 0.1]).reshape(2,1) # initial weights
learning_rate = 0.1
bias = -0.1
