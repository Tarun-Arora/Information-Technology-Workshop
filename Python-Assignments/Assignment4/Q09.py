import numpy as np
v = [[10, 40], [30, 20]]
print("Original array : ", v)
print("Sorted the array along the first axis: ", np.sort(v, axis=0))
print("Sorted the array along the last axis: ", np.sort(v, axis=1))
print("Sorted the flattened array:", np.sort(np.array(v).flatten()))