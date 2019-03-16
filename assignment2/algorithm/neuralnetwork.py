import numpy as np

class NeuralNetwork():

    def __init__(self):
        self.P = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4) # input 
        self.t = np.array([0, 0, 0, 1])
        self.weights = np.array([0.3, -0.1]).reshape(1,2) # initial weights
        self.learning_rate = 0.1
        self.bias = -0.2
        self.c = self.P.shape[1]
        self.maxIterations = 30


    def update_weights(self, w, rate, e, p):
        return w + rate*p*e

    def calculate_error(self, t, a):
        return t-a

    def update_bias(self, b, e, rate):
        return b + rate * b * e

    def execute(self):
        adjustmentDone = False
        iteration = 0
        while not adjustmentDone:
            estimated_output = np.empty([4])
            for i in range(self.c):
                net = np.matmul(self.weights, self.P[:, i]) + self.bias
                a = np.heaviside(net, 1)
                estimated_output[i] = a
                e = self.calculate_error(self.t[i], a)
                self.weights = self.update_weights(self.weights, self.learning_rate, e, self.P[:,i])
                self.bias = self.update_bias(self.bias, self.learning_rate, e)
        
                print("e on c={}: {}\r\n".format(i, e))
                print("weights on c={}: {}\r\n".format(i, self.weights))
                print("bias on c={}: {}\r\n".format(i, self.bias))
                print("---------------------\r\n\r\n\r\n")

            if(np.array_equal(estimated_output, self.t)):
                adjustmentDone = True
                print("Adjustment done by finding correct parameters")
            elif iteration >= self.maxIterations:
                adjustmentDone = True
                print("Adjustment done by reaching max iterations")
    
            iteration += 1