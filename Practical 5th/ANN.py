import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

np.random.seed(42)
input_size = 2
hidden_size = 3
output_size = 1

weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

bias_hidden = np.zeros((1, hidden_size))
bias_output = np.zeros((1, output_size))

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])


learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)
    output_layer_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    error = y - predicted_output

    output_error = error * sigmoid_derivative(predicted_output)
    hidden_layer_error = output_error.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_output)

    weights_hidden_output += hidden_output.T.dot(output_error) * learning_rate
    weights_input_hidden += X.T.dot(hidden_layer_error) * learning_rate

    bias_output += np.sum(output_error, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_layer_error, axis=0, keepdims=True) * learning_rate

test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

hidden_input_test = np.dot(test_input, weights_input_hidden) + bias_hidden
hidden_output_test = sigmoid(hidden_input_test)
output_layer_input_test = np.dot(hidden_output_test, weights_hidden_output) + bias_output
predicted_output_test = sigmoid(output_layer_input_test)

print("\nPredicted Output:")
print(predicted_output_test)
print("\n")
