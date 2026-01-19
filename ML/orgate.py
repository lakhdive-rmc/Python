import numpy as np

# Perceptron prediction
def predict(X):
    w = np.array([1, 1])
    b = -0.5
    return 1 if np.dot(X, w) + b >= 0 else 0

# Test OR gate
print("X1 X2 Y")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(x1, x2, predict(np.array([x1, x2])))
