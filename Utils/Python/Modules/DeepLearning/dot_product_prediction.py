import numpy as np
import matplotlib
from isapi.samples.redirector_with_filter import proxy

# ref : https://realpython.com/python-ai-neural-network/

input_vector_1 = np.array([1.66, 1.56])
input_vector_2 = np.array([2, 1.5])

weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def make_prediction(input_vector, weights, bias):
   layer_1 = np.dot(input_vector, weights) + bias
   layer_2 = sigmoid(layer_1)
   return layer_2

def sigmoid(x):
   return 1 / (1 + np.exp(-x))

def print_prediction_result(input_vector, weights, bias, prediction):
    print(f"Input vector: {input_vector}")
    print(f"weights_1: {weights}")
    print(f"bias: {bias}")
    print(f"The prediction result is: {prediction}")

prediction_1 = make_prediction(input_vector_1, weights_1, bias)
print_prediction_result(input_vector_1, weights_1, bias, prediction_1)

prediction_2 = make_prediction(input_vector_2, weights_1, bias)
print_prediction_result(input_vector_2, weights_1, bias, prediction_2)


target = 0
input_vector_3 = np.array([2, 1.5])
prediction_3 = make_prediction(input_vector_3, weights_1, bias)
mse = np.square(prediction_3 - target)
print(f"Prediction: {prediction_3}; Error: {mse}")

derivative = 2 * (prediction_3 - target)
print(f"The derivative is {derivative}")

weights_1 = weights_1 - derivative
prediction_4 = make_prediction(input_vector_3, weights_1, bias)
error = np.square(prediction_4 - target)
print(f"Prediction: {prediction_4}; Error: {error}")


weights = np.array([1.45, -0.66])
def recursive_training(input_vector, weights, bias, target, allowed_error):
    prediction = make_prediction(input_vector, weights, bias)

    if target < prediction:
        derivative = 2 * (prediction - target)
    else:
        derivative = 2 * (prediction + target)

    error = (prediction - target) ** 2

    if error > allowed_error:
        weights = weights - derivative
        recursive_training(input_vector, weights, bias, target, allowed_error)
    else:
        print(f"Prediction: {prediction}; weight: {weights}; Error: {error}")

recursive_training(input_vector_3, weights, bias, target, 0.001)
recursive_training(input_vector_3, weights, bias, target, 0.0001)