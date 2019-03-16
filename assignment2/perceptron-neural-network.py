import numpy as np

P = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4) # input 
t = np.array([0, 0, 0, 1])
weights = np.array([0.3, -0.1]).reshape(1,2) # initial weights
learning_rate = 0.1
bias = -0.2
c = P.shape[1]
maxIterations = 30

def update_weights(w, rate, e, p):
    return w + rate*p*e

def calculate_error(t, a):
    return t-a

def update_bias(b, e, rate):
    return b + rate * b * e

adjustmentDone = False
iteration = 0
while not adjustmentDone:
    estimated_output = np.empty([4])
    for i in range(c):
        net = np.matmul(weights, P[:, i]) + bias
        a = np.heaviside(net, 1)
        estimated_output[i] = a
        e = calculate_error(t[i], a)
        weights = update_weights(weights, learning_rate, e, P[:,i])
        bias = update_bias(bias, learning_rate, e)
        
        print("e on c={}: {}\r\n".format(i, e))
        print("weights on c={}: {}\r\n".format(i, weights))
        print("bias on c={}: {}\r\n".format(i, bias))
        print("---------------------\r\n\r\n\r\n")

    if(np.array_equal(estimated_output, t)):
        adjustmentDone = True
        print("Adjustment done by finding correct parameters")
    elif iteration >= maxIterations:
        adjustmentDone = True
        print("Adjustment done by reaching max iterations")
    
    iteration += 1


