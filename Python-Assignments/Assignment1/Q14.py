arr=[x for x in input("\nEnter all elements of the array: ").split(' ')]
x=input('Input the element you want to find no. of occurences of: ')
c=0
for i in arr:
    if i==x:
        c+=1
print(f"Number of occurences of {x} in this array are {c}")