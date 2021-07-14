import pandas as pd
a = pd.Series([2, 4, 6, 8, 10])
b = pd.Series([1, 3, 5, 7, 9])
print("Add :", list(a + b))
print("Subtract :", list(a - b))
print("Multiply :", list(a * b))
print("Divide :", list(a / b))