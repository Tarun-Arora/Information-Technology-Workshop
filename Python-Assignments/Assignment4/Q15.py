import numpy as np
x = np.array([10, 10, 20, 30, 30])
print(x)
y = np.array([0, 40])
x.put([0, 4], y)
print("Array x after puts two values:", x)