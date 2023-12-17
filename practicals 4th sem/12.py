import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, output):
        self.error = output - y
        self.delta2 = self.error * self.sigmoid_derivative(output)
        self.error_hidden = self.delta2.dot(self.W2.T)
        self.delta1 = self.error_hidden * self.sigmoid_derivative(self.a1)
        
        # Update weights and biases
        self.W2 -= self.a1.T.dot(self.delta2)
        self.b2 -= np.sum(self.delta2, axis=0)
        self.W1 -= X.T.dot(self.delta1)
        self.b1 -= np.sum(self.delta1, axis=0)
        
    def train(self, X, y, epochs):
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
        
    def predict(self, X):
        return np.round(self.forward(X))
        

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

input_size = X.shape[1]
hidden_size = 4
output_size = y.shape[1]
epochs = 10000

# Create and train the neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(X, y, epochs)

# Make predictions
predictions = nn.predict(X)
print("Predictions:")
print(predictions)
