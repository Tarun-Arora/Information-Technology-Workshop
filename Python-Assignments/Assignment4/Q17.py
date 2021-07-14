import numpy as np
import pandas as pd
arr = np.array([10, 20, 30, 40, 50])
print("Numpy Array :", arr)
series = pd.Series(arr)
print("Converted pandas series is:\n", series,sep='')