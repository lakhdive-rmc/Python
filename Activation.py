# %%
import math 
def sigmoidal(x) : 
    res = 1 / ( 1+ math.exp(-x))
    return res
sigmoidal(0.3)

# %%
import numpy as np
x = np.array([1, 0.8, 0.9, 0.4])
w = np.array([0.35, 0.1, 0.2, -0.2])
y = np.dot(x,w)
print(f'sum = {y}')
res=sigmoidal(y)
print(f'output = {res:.2}')     

# %%
def bipolarigmoidal(x) : 
    res = (1 - math.exp(-x))  / ( 1+ math.exp(-x))
    return res
bipolarigmoidal(0.3)
bipolarigmoidal(y)


