import numpy as np

class NeuralNetwork():

    def __init__(self, weights, learning_rate, bias):
        self.P = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4)
        self.desired_output = np.array([0, 1, 1, 1])
        self.weights = weights # initial weights
        self.learning_rate = learning_rate
        self.bias = bias
        self.c = self.P.shape[1]
        self.maxIterations = 30


    def update_weights(self, w, rate, e, p):
        return w + rate*p*e

    def calculate_error(self, desired, actual):
        return desired-actual

    def update_bias(self, b, e, rate):
        return b + rate * b * e

    def execute(self):
        adjustmentDone = False
        iteration = 0
        while not adjustmentDone:
            estimated_output = np.empty([4])
            for i in range(self.c):
                net = np.matmul(self.weights, self.P[:, i]) + self.bias
                activation_result = np.heaviside(net, 1)
                estimated_output[i] = activation_result
                e = self.calculate_error(self.desired_output[i], activation_result)
                self.weights = self.update_weights(self.weights, self.learning_rate, e, self.P[:,i])
                self.bias = self.update_bias(self.bias, self.learning_rate, e)

            if(np.array_equal(estimated_output, self.desired_output)):
                adjustmentDone = True
                print("Adjustment done by finding correct parameters\r\nIt took {} iterations to complete".format(iteration))
            elif iteration >= self.maxIterations:
                adjustmentDone = True
                print("Adjustment done by reaching max iterations")
    
            iteration += 1
        
        print("------ FINAL RESULT ------\r\n")
        print("Weights:\r\n \t w_1 = {}\r\n \t w_2 = {}\r\n".format(self.weights[0,0], self.weights[0,1]))