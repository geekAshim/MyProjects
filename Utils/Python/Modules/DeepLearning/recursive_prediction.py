import numpy as np

# ref : https://realpython.com/python-ai-neural-network/

def make_prediction(input_vector, weights, bias):
   layer_1 = np.dot(input_vector, weights) + bias
   layer_2 = sigmoid(layer_1)
   return layer_2

def sigmoid(x):
   return 1 / (1 + np.exp(-x))

target = 0
input_vector = np.array([2, 1.5])
bias = np.array([0.0])
weights = np.array([1.45, -0.66])

def recursive_training(vector, weights, bias, target, allowed_error, layer):
    layer = layer + 1
    prediction = make_prediction(vector, weights, bias)

    if target < prediction:
        derivative = 2 * (prediction - target)
    else:
        derivative = 2 * (prediction + target)

    error = (prediction - target) ** 2

    if error > allowed_error:
        weights = weights - derivative
        recursive_training(vector, weights, bias, target, allowed_error, layer)
    else:
        print(f"Prediction: {prediction}; weight: {weights}; Error: {error}; layer: {layer}")

recursive_training(input_vector, weights, bias, target, 0.001, 0)
recursive_training(input_vector, weights, bias, target, 0.0001, 0)
recursive_training(input_vector, weights, bias, target, 0.00001, 0)
recursive_training(input_vector, weights, bias, target, 0.000001, 0)