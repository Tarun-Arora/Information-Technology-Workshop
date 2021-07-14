import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array(['Red', 'Green', 'White', 'Orange'])
c = np.array([12.20, 15, 20, 40])
r = np.core.records.fromarrays([a, b, c])
print(r[0])
print(r[1])
print(r[2])