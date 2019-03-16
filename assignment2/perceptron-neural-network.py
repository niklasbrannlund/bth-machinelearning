import numpy as np

P = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4) # input 
t = np.array([0, 0, 0, 1])
weights = np.array([0.3, -0.1]).reshape(1,2) # initial weights
learning_rate = 0.1
bias = -0.2
c = P.shape[1]

def update_weights(w, rate, e, p):
    return w + rate*np.matmul(p, np.transpose(e))

def calculate_error(t, a):
    return t-a

def update_bias(b, e, rate):
    return b + rate * e


for i in range(5):
    net = np.matmul(weights, P) + bias
    a = np.heaviside(net, 1)
    print("-------------")
    print(t)
    print("\r\n\r\n")
    if(np.array_equal(a,t)):
        print("success")

    e = calculate_error(t, a)
    weights = update_weights(weights, learning_rate, e, P)
    bias = update_bias(bias, learning_rate, e)

