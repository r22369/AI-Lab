import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None

    def train(self, X, y):
        self.weights = np.zeros(X.shape[1] + 1)
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update

    def predict(self, X):
        return np.where(np.dot(X, self.weights[1:]) + self.weights[0] > 0, 1, 0)

X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
y = np.array([1, 0, 0, 0])
perceptron = Perceptron()
perceptron.train(X, y)
print("Trained weights:", perceptron.weights)
