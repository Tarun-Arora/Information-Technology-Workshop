arr=[x for x in input('\nEnter the list: ').split()]
n=int(input('Enter the value of n: '))
v=[]
for i in range(min(len(arr),n)):
    v.append([])
for i in range(len(arr)):
    (v[i%n]).append(arr[i])
print('Resultant List:\n',v,sep='')