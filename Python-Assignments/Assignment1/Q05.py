arr=[x for x in input("Enter string to be sorted: ")]
arr.sort()
s=""
for i in arr:
    s+=i
print("The sorted string is:",s)