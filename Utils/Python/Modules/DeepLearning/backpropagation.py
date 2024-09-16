import numpy as np

from Utils.Python.Modules.DeepLearning.dot_product_prediction import target

# ref : https://realpython.com/python-ai-neural-network/

input_vector_1 = np.array([1.66, 1.56])
input_vector_2 = np.array([2, 1.5])


target = 0

def make_prediction(input_vector, weights, bias):
   layer_1 = np.dot(input_vector, weights) + bias
   layer_2 = sigmoid(layer_1)
   return layer_2

def sigmoid(x):
   return 1 / (1 + np.exp(-x))

weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

prediction_layer1 = make_prediction(input_vector_1, weights_1, bias)
error_weight_layer1 = np.square(prediction_layer1 - target)
weights_1 = weights_1 - error_weight_layer1

prediction_layer2 = make_prediction(input_vector_1, weights_1, bias)
error_weight_layer2 = np.square(prediction_layer2 - target)
error_bias = error_weight_layer2 * prediction_layer1 * bias
weights_1 = weights_1 - error_weight_layer2

bias_layer3 = bias - error_bias

prediction_layer3 = make_prediction(input_vector_1, weights_1, bias)
error_weights_layer3 = np.square(prediction_layer3 - target)
weights_1 = weights_1 - error_weights_layer3
error_bias_layer3 = error_weights_layer3 * prediction_layer2 * bias
print(f"PredictionLayer3: {prediction_layer3}; weightsLayer2: {weights_1}; bias_layer2: {bias}; biasLayer3: {bias_layer3}")



