import sys
x=input("Enter the object you want to get size of: ")
print(f"Memory size of '{x}'={sys.getsizeof(x)} bytes")