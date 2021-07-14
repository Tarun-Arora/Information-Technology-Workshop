import array
arr=array.array('i',[int(x) for x in input().split(' ')])
print(type(arr),arr)
#conversion
l=arr.tolist()
print(type(l),l)