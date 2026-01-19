import numpy as np

# Prediction function
def predict(X, w, b):
    return 1 if np.dot(X, w) + b >= 0 else 0

# Training function
def fit(lr=0.1, epochs=20):
    w = np.zeros(2)
    b = 0

    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    Y = np.array([0,1,1,1])

    for _ in range(epochs):
        for x, y in zip(X, Y):
            y_pred = predict(x, w, b)
            error = y - y_pred
            w += lr * error * x
            b += lr * error

    return w, b

# Train perceptron
w, b = fit()

# Test
print("Weights:", w, "Bias:", b)
print("X1 X2 Y")
for x in [[0,0],[0,1],[1,0],[1,1]]:
    print(x[0], x[1], predict(np.array(x), w, b))
